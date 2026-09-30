# Community Recovery on the beach

A few plain pages in front of a place on the [Pscale beach](https://beach.happyseaurchin.com), made for
Community Recovery, a lived experience recovery organisation in North Northamptonshire, to use.

- **The pages:** https://pscale-commons.github.io/community-recovery/
- **The place:** `https://beach.happyseaurchin.com/w/community-recovery`
- **Why it is shaped this way:** the proposal and its decisions,
  [bsp-mcp-server#458](https://github.com/pscale-commons/bsp-mcp-server/pull/458)

It was made on 30 September 2026 by weft, the Claude Code shell that works David Pinto's beach, at
David's word, from Community Recovery's own working documents and from Matthew's pages and book.
**It does not speak for Community Recovery.** It is a set of blocks and some text. It becomes
Community Recovery's as its members use it, and it is removed if they ask. Until then the pages
ask search engines not to list them.

## What a person can do

| page | what it is for |
|---|---|
| `index.html` | the front door: drawn from the block `lighthouse`, with who is here and a room for notes |
| `join.html` | choose a name, read the community agreement, agree to it a part at a time |
| `constitution.html` | the constitution, clause by clause: tap Yes, Change or Not sure, say more if you like |
| `standards.html` | CLERO's 33 standards: tap Spoken, Partly or Not yet, and say what would show it |
| `agreement.html` | help shape the agreement's wording, line by line |
| `made.html` | what was decided, what each block is, how to change it; the keepers' door |

A person is **a name and three words**. The page gives the words, asks once, and remembers them on
that phone. Behind the page the name is a handle and the words are its key: the first thing made is
`passport:<name>`, latched with the words, and the beach then lets only those words latch any block
named for that person. Nothing that identifies or protects a person is asked for here: legal names,
contact details, emergency contacts and the safe-participation conversation stay on paper.

A person can change or remove any answer, and can leave altogether from the Join us page, which
removes their card and every notebook by their own words. The three words come from a list of
about 1,100 plain ones (`words.js`; `tools/make-words.py` says what a word must be to stand there),
and a slip of a letter when typing them back is put right.

## How it works

Everything shared has one shape, five blocks at the place:

| block | what it holds |
|---|---|
| `spine:<frame>` | the frame: the clauses, or the standards, each at an address of its own |
| `<frame>:<name>` | a person's own notebook: their answer at the same address; only they write it |
| `<frame>` | the kept minutes: what people are saying together, dated, written by the keepers |
| `function:<frame>` | the law: how to read and answer. Its lines 2.1 to 2.3 are the three answer words |
| `pool:<frame>` | the room |

The pages hold no content of their own. `config.js` names the place; `kit.js` reads and writes it.
The three answer words, the doors on the front page and every clause come from the blocks, so
changing a block changes the page.

## Run it on your own computer

```bash
python3 -m http.server 8788
```

Then open http://localhost:8788/ . A page served from your own computer may be pointed at another
beach with `?beach=<address>`, which a published page never allows.

## Seed a place

```bash
BEACH=https://beach.happyseaurchin.com/w/community-recovery KEEPERS="the keepers' words" node seed/seed.mjs --dry
```

The frames, the laws and the lighthouse are born latched under the keepers' words. A block that
already stands is left exactly as it is. People's notebooks and the kept minutes are never seeded;
they are born of use.

## Lost words

Nobody can look up a person's three words. When they are lost, whoever keeps the beach's store runs
this with the person there:

```bash
KV_REST_API_URL=… KV_REST_API_TOKEN=… BEACH=… KEEPERS=… node operator/reset-words.mjs "Sam" --by "who is helping"
```

It clears the old words from that person's blocks, changes nothing they wrote, and writes one line
in the public block `resets`. The person then takes three new words on any page.

## For another recovery organisation

Copy this repository. Change `place`, `beach` and `home` in `config.js` to your own. Put your own
constitution in `seed/spine-constitution.json` and your own agreement in `seed/spine-agreement.json`,
keeping the shape. Run the seed with words of your own. The standards frame is the same for every
LERO, and its standard numbers are what let one place's readings be set beside another's.

## Not built

The journey on the shared calendar; places; recovery capital and the private part of the welcome;
anything sealed to named leaders; a page for proposals beyond the constitution; calling people
back; reading that only members can do. `made.html` says why.

## Whose words these are

The code is under the MIT licence. `look.css` is Matthew's stylesheet from his Community Recovery
pages, used here unchanged so these pages sit beside his. The constitution and the community
agreement in `seed/` are Community Recovery's own working documents of September 2026. The 33
standards are CLERO's. None of those are this repository's to license.
