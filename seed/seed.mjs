#!/usr/bin/env node
// seed.mjs — writes this kit's blocks to a place on a beach.
//
//   BEACH=https://beach.happyseaurchin.com/w/community-recovery KEEPERS="the keepers' words" node seed/seed.mjs
//   add --dry to see what would be written and write nothing
//
// The frames, the laws and the lighthouse are born latched under the keepers' words; the rooms are
// born open, as rooms are. A block that already stands is left exactly as it is and reported:
// nothing here ever replaces anything. People's own notebooks and the kept minutes are never
// seeded. They are born of use.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const here = path.dirname(fileURLToPath(import.meta.url));
const BEACH = (process.env.BEACH || '').replace(/\/+$/, '');
const KEEPERS = process.env.KEEPERS || '';
const dry = process.argv.includes('--dry');
if (!BEACH) { console.error('set BEACH to the place, e.g. https://beach.happyseaurchin.com/w/community-recovery'); process.exit(2); }
if (!KEEPERS && !dry) { console.error('set KEEPERS to the keepers\' words'); process.exit(2); }
const wire = BEACH + '/.well-known/pscale-beach';
const manifest = JSON.parse(fs.readFileSync(path.join(here, 'manifest.json'), 'utf8'));
const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
let born = 0, stand = 0, differ = 0, failed = 0;
for (const m of manifest) {
  const content = JSON.parse(fs.readFileSync(path.join(here, m.file), 'utf8'));
  const got = await fetch(wire + '?block=' + encodeURIComponent(m.block), { headers: { Accept: 'application/json' } });
  if (got.status === 200) {
    const standing = await got.json();
    if (same(standing, content)) { stand++; console.log('  stands   ', m.block); }
    else { differ++; console.log('  DIFFERS  ', m.block, '(left as it is)'); }
    continue;
  }
  if (got.status !== 404) { failed++; console.log('  UNREAD   ', m.block, got.status); continue; }
  if (dry) { console.log('  would be born', m.block, m.latch === 'keepers' ? '(latched)' : '(open)'); continue; }
  const body = { block: m.block, content };
  if (m.latch === 'keepers') body.new_lock = KEEPERS;
  const r = await fetch(wire + '?block=' + encodeURIComponent(m.block), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  const j = await r.json().catch(() => ({}));
  if (r.ok && j.ok !== false) { born++; console.log('  born     ', m.block, m.latch === 'keepers' ? '(latched)' : '(open)'); }
  else { failed++; console.log('  FAILED   ', m.block, r.status, JSON.stringify(j).slice(0, 160)); }
}
console.log(`\n${born} born · ${stand} already standing · ${differ} standing and different · ${failed} failed · at ${BEACH}`);
process.exit(failed ? 1 : 0);
