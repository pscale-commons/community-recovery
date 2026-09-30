#!/usr/bin/env node
// reset-words.mjs — for whoever keeps the beach's store, when a person has lost their three words.
//
// Run it with the person there and asking. It clears the old words (the latches) from the blocks
// named for that person at one place, changes nothing they wrote, and writes one line in the block
// `resets` at that place, where the person and anyone else can read that it happened. The person
// then opens any page, taps "I already have a name", then "I've lost my words", and takes three
// new ones. Whoever ran this holds nothing of theirs afterwards.
//
//   KV_REST_API_URL=… KV_REST_API_TOKEN=… \
//   BEACH=https://beach.happyseaurchin.com/w/community-recovery KEEPERS="the keepers' words" \
//   node operator/reset-words.mjs "Sam" --by "the name of whoever is helping"  [--dry]
//
// KV_REST_API_URL and KV_REST_API_TOKEN are the store's own (the beach's Upstash), which only its
// keeper has. --dry shows what would be cleared and clears nothing.
const args = process.argv.slice(2);
const dry = args.includes('--dry');
const byAt = args.indexOf('--by');
const by = byAt >= 0 ? args[byAt + 1] : '';
const asked = args.find((a, i) => !a.startsWith('--') && i !== byAt + 1);
const BEACH = (process.env.BEACH || '').replace(/\/+$/, '');
const KEEPERS = process.env.KEEPERS || '';
const KV = (process.env.KV_REST_API_URL || '').replace(/\/+$/, '');
const TOKEN = process.env.KV_REST_API_TOKEN || '';
function stop(msg) { console.error(msg); process.exit(2); }
if (!asked) stop('say whose words: node operator/reset-words.mjs "Sam" --by "who is helping"');
if (!by) stop('say who is helping, with --by: it is written in the record');
if (!BEACH) stop('set BEACH to the place, e.g. https://beach.happyseaurchin.com/w/community-recovery');
if (!dry && (!KV || !TOKEN)) stop('set KV_REST_API_URL and KV_REST_API_TOKEN: the store\'s own');
if (!dry && !KEEPERS) stop('set KEEPERS to the keepers\' words: the record is kept under them');

const wire = BEACH + '/.well-known/pscale-beach';
// the store keys a place by its address without the scheme: beach.example.org/w/place
const origin = BEACH.replace(/^https?:\/\//, '');
const lockKey = (block) => `pscale-beach-v2:${origin}:locks:${block}`;
async function kv(command) {
  const r = await fetch(KV, { method: 'POST', headers: { Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' }, body: JSON.stringify(command) });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || j.error) throw new Error('store: ' + (j.error || r.status));
  return j.result;
}
async function post(body) {
  const r = await fetch(wire + '?block=' + encodeURIComponent(body.block), { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  const j = await r.json().catch(() => ({}));
  return { ok: r.ok && j.ok !== false && !j.error, status: r.status, data: j };
}

const idx = await (await fetch(wire, { headers: { Accept: 'application/json' } })).json();
const blocks = Array.isArray(idx.blocks) ? idx.blocks : Object.keys(idx.blocks || {});
const people = blocks.filter((b) => b.startsWith('passport:')).map((b) => b.slice(9));
const name = people.find((p) => p.toLowerCase() === asked.toLowerCase());
if (!name) stop(`nobody at ${BEACH} is called "${asked}". Names here: ${people.join(', ') || '(none)'}`);
// every block named for the person: their card, and a notebook for each frame
const theirs = blocks.filter((b) => b.endsWith(':' + name) && !b.startsWith('sed:') && !b.startsWith('grain:'));
console.log(`${name} at ${BEACH}: ${theirs.length} block(s)`);
let cleared = 0;
for (const b of theirs) {
  if (dry) { console.log('  would clear the words on', b); continue; }
  const n = await kv(['DEL', lockKey(b)]);
  cleared += n ? 1 : 0;
  console.log(n ? '  cleared  ' : '  was open ', b);
}
if (dry) { console.log('\nnothing was changed (--dry)'); process.exit(0); }
if (!cleared) { console.log(`\nnothing to clear: ${name}'s blocks were already open. Nothing was recorded.`); process.exit(0); }

// the record, where the person can read it
const stamp = new Date().toISOString();
const line = `${name}’s words were cleared on ${stamp.slice(0, 10)}, with ${name} there and asking, by ${by}. ${name} then chooses new words, which nobody else holds. Nothing ${name} wrote was changed.`;
// born latched under the keepers' words the first time it is needed, then only ever added to
if (!blocks.includes('resets')) {
  await post({ block: 'resets', new_lock: KEEPERS, content: { _: 'RESETS \u2014 every time a person\u2019s lost words were cleared at this place: whose, when, and who helped. Words are cleared only with the person there and asking; the person chooses new ones themselves, and whoever helped holds nothing of theirs.' } });
}
const r = await post({ block: 'resets', append: true, secret: KEEPERS, content: { _: line, 1: by, 3: stamp } });
console.log(r.ok ? '  recorded at the block `resets`' : `  NOT recorded (${r.status} ${JSON.stringify(r.data).slice(0, 120)})`);
console.log(`\n${cleared} cleared. Now, with ${name}: open any page, tap "I already have a name", then "I've lost my words".`);
process.exit(r.ok ? 0 : 1);
