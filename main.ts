// "17 November 2026 — World News in One Image" (make.fun news-image-20261117).
//
// The picture itself is the entry: a hand-drawn infographic (built with
// draw.py in this repo) that sums up Tuesday 17 November 2026 — Ukraine's
// second strike on the Crimea bridge, Iran's drone attack on the US radar
// base in Bahrain, the Xi–Trump–Putin meeting confirmed for Shenzhen,
// tankers mined near Hormuz, five European nations' Rwanda return hub,
// the US banking outage, plus Japan's jet scramble and Voyager 1.
//
// The grader runs this program with no network in a sandbox; all it has to
// do is place the finished image at $MAKEFUN_OUTPUT_DIR/entry.png (or
// /output/entry.png when that variable is unset). Copying the file keeps
// the run byte-for-byte deterministic: both runs write identical bytes.

import { copyFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = new URL('./entry.png', import.meta.url);
if (!existsSync(source)) {
  throw new Error('entry.png is missing from the repository');
}
copyFileSync(source, join(outDir, 'entry.png'));
