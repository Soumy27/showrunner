#!/usr/bin/env node
// Draws an HTML page frame by frame in headless Chrome and encodes it with ffmpeg.
// The page must expose window.ready (a promise) and window.seek(seconds).
//   node render-frames.mjs page.html out.mp4 --seconds 30 [--audio beat.wav] [--size 1080x1920]
//   node render-frames.mjs page.html --stills 1,2,5 --out-dir frames/
import { spawn } from 'node:child_process';
import { mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

const args = process.argv.slice(2);
const opt = (name, fallback) => {
  const i = args.indexOf(`--${name}`);
  return i >= 0 ? args[i + 1] : fallback;
};
const page = resolve(args[0]);
const stills = opt('stills');
const out = stills ? null : resolve(args[1]);
const seconds = Number(opt('seconds', 30));
const audio = opt('audio');
const [W, H] = opt('size', '1080x1920').split('x').map(Number);
const FPS = 30;
const CHROME = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const port = 9400 + (process.pid % 500);

const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${port}`, `--window-size=${W},${H}`,
  '--force-device-scale-factor=1', '--hide-scrollbars', '--allow-file-access-from-files', '--no-first-run',
  `--user-data-dir=${mkdtempSync(join(tmpdir(), 'reel-'))}`, 'about:blank'], { stdio: 'ignore' });
chrome.on('error', (e) => { console.error(`cannot start Chrome: ${e.message}`); process.exit(2); });

let target;
for (let i = 0; i < 80 && !target; i++) {
  await new Promise((r) => setTimeout(r, 250));
  try {
    target = (await (await fetch(`http://127.0.0.1:${port}/json`)).json()).find((t) => t.type === 'page');
  } catch {}
}
if (!target) { console.error('Chrome did not answer'); chrome.kill(); process.exit(2); }
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((r) => (ws.onopen = r));
let id = 0;
const waiting = new Map();
ws.onmessage = (m) => {
  const d = JSON.parse(m.data);
  if (d.id && waiting.has(d.id)) { waiting.get(d.id)(d); waiting.delete(d.id); }
};
const send = (method, params = {}) => new Promise((r) => {
  waiting.set(++id, r);
  ws.send(JSON.stringify({ id, method, params }));
});
const run = async (expression) => {
  const r = await send('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
  if (r.result?.exceptionDetails) {
    console.error(`page error: ${JSON.stringify(r.result.exceptionDetails).slice(0, 600)}`);
    chrome.kill();
    process.exit(2);
  }
  return r.result?.result?.value;
};
await send('Page.enable');
await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile: false });
await send('Page.navigate', { url: `file://${page}` });
await new Promise((r) => setTimeout(r, 1200));
await run('window.ready');
const shot = async (t, format = 'jpeg') => {
  await run(`seek(${t})`);
  const params = format === 'jpeg' ? { format, quality: 96 } : { format };
  return Buffer.from((await send('Page.captureScreenshot', params)).result.data, 'base64');
};

if (stills) {
  const dir = resolve(opt('out-dir', '.'));
  mkdirSync(dir, { recursive: true });
  for (const t of stills.split(',').map(Number)) writeFileSync(join(dir, `still-${t}.png`), await shot(t, 'png'));
  console.log(`wrote stills to ${dir}`);
} else {
  const inputs = ['-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-'];
  if (audio) inputs.push('-i', resolve(audio));
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', ...inputs, '-c:v', 'libx264', '-preset', 'medium', '-crf', '19',
    '-pix_fmt', 'yuv420p', ...(audio ? ['-c:a', 'aac', '-b:a', '192k', '-shortest'] : []), '-movflags', '+faststart', out],
    { stdio: ['pipe', 'inherit', 'inherit'] });
  const frames = Math.round(seconds * FPS);
  for (let f = 0; f < frames; f++) {
    const b = await shot(f / FPS);
    if (!ff.stdin.write(b)) await new Promise((r) => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await new Promise((r) => ff.on('close', r));
  console.log(`wrote ${out}: ${seconds}s, ${W}x${H}, ${FPS} fps`);
}
ws.close();
chrome.kill();
process.exit(0);
