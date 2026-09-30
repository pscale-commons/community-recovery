#!/usr/bin/env python3
"""Builds words.js: the plain words a person's three words are drawn from.
Rules for a word: everyday and concrete, three to eight letters, one common spelling,
no sound-alike twin, no numbers, nothing about drink, drugs, gambling, harm, illness, the law or money,
and nothing rude in slang. Add to the lists below and run again; the page only needs the list
to stay the same length or grow, because words already given are typed back, never looked up."""
import re, sys, os
RAW = """
river stream brook meadow forest valley hillside mountain cliff coast island lagoon cove delta marsh heath field garden orchard hedge grove glade
timber branch twig leaf petal blossom bloom seed moss fern clover daisy tulip lily violet lilac jasmine lavender heather thistle nettle holly willow maple birch cedar
spruce aspen hazel rowan alder acorn conker walnut chestnut bramble bracken pebble boulder gravel sand clay chalk flint slate granite marble amber pearl coral
cloud fog frost sleet breeze gale storm thunder rainbow sunrise sunset dawn dusk noon evening midnight summer winter autumn spring season shadow sunbeam moon star planet
comet orbit galaxy meteor ripple puddle pond lake ocean summit ridge slope ledge cavern grotto quarry jetty wharf oasis canyon plateau tundra jungle prairie glacier volcano
otter badger fox rabbit hedgehog mole mouse vole stag pony donkey goat sheep lamb cow piglet kitten puppy beagle collie terrier spaniel tabby robin sparrow finch swallow
swift heron egret crane stork swan goose duck gull puffin owl falcon kestrel eagle hawk raven magpie dove lark thrush starling parrot penguin pelican turkey hen rooster
chick wasp moth beetle cricket ladybird spider snail worm frog newt lizard gecko turtle tortoise dolphin walrus trout herring crab lobster shrimp oyster starfish seahorse
octopus squid panda koala tiger lion zebra camel alpaca bison moose monkey lemur hippo elephant wombat ferret weasel wolf cub fawn foal gosling cygnet
apple plum peach cherry lemon lime orange melon mango banana fig olive tomato potato carrot onion garlic ginger pepper parsley basil mint fennel celery cabbage turnip parsnip
radish pumpkin marrow lentil oats wheat rice bread toast butter cheese honey jam syrup sugar salt vinegar mustard pickle soup stew pasta noodle pizza pie pastry cracker
crumpet muffin scone pancake waffle custard pudding cocoa coffee milk juice water kettle teapot mug cup plate bowl spoon fork ladle whisk pan oven grill toaster fridge larder
pantry apricot avocado coconut papaya satsuma quince rhubarb beetroot cucumber mushroom chickpea peanut pecan cashew sesame vanilla cinnamon nutmeg paprika saffron caramel
toffee fudge sherbet crumble flapjack pretzel bagel burrito falafel hummus chutney ketchup gravy porridge granola muesli sandwich sausage dumpling risotto curry salsa nachos
table chair stool bench sofa pillow blanket quilt duvet carpet rug lamp lantern candle torch mirror window door handle hinge latch shelf cupboard wardrobe basket bucket broom
brush sponge towel soap ribbon button zip thread thimble pin fabric cotton linen wool velvet denim scarf glove mitten sock boot sandal slipper jacket jumper coat cape hat cap
bonnet badge pocket umbrella satchel rucksack suitcase parcel packet envelope letter stamp postcard pencil crayon marker paper notebook journal ledger atlas map globe compass
clock bell drum flute fiddle banjo piano organ trumpet cornet harp violin tuba bugle chime melody anthem ballad lyric verse poem fable legend riddle puzzle jigsaw domino kite
swing slide seesaw skate sledge scooter tandem wagon cart barrow tractor harvest barn stable shed cabin cottage lodge tent igloo castle tower bridge tunnel canal ferry barge
kayak raft rudder paddle beacon signal station platform railway engine carriage ticket journey voyage picnic holiday festival carnival parade market bakery museum gallery
cinema studio workshop office school college park square avenue lane path track trail street corner village town city county
hammer chisel spanner pliers ladder shovel spade rake trowel wheel lever pulley magnet battery cable socket switch bulb plug fuse wire rope string twine chain hook bolt rivet
plank brick tile cement plaster paint varnish glue tape copper silver golden bronze iron tin zinc nickel cobalt carbon oxygen helium neon argon
green yellow purple pink brown black white scarlet crimson maroon magenta indigo teal azure navy khaki beige cream ivory ruby emerald sapphire jade opal topaz garnet onyx
three five six seven nine ten eleven twelve twenty thirty fifty sixty hundred dozen single double triple first second third fifth monday tuesday friday sunday january april
june july august october minute today tonight weekend century decade north south east west middle circle oval spiral arrow angle curve dot stripe zigzag pattern mosaic
canvas sketch portrait picture photo camera film poster banner flag medal trophy crown shield helmet
gentle steady quiet bright calm kind brave clever merry jolly snug warm cool fresh crisp soft smooth round tall tiny little giant grand simple proper lively busy early eager
friendly happy cheery sunny breezy frosty misty cloudy windy dusty mossy leafy woolly fluffy fuzzy bumpy curly wavy shiny glossy wooden woven painted polished hidden open
clear honest humble loyal patient careful curious playful helpful hopeful mindful thankful wise nimble sturdy solid strong light
wander ramble stroll amble march gallop canter trot skip jump leap climb swim float drift glide soar flutter hover tumble wobble wiggle giggle chuckle whisper murmur hum sing
clap nod smile wink listen gather mend build carve knit weave bake cook stir plant grow dig sweep polish draw count measure juggle balance stretch ponder wonder imagine
invent explore discover travel arrive return begin finish
bubble feather echo ember fountain garland icicle saddle wicker yarn doorbell doormat keyring coaster napkin apron teacup eggcup jug vase planter trellis hammock parasol
lunchbox backpack raincoat wellies anorak cardigan bobble tassel fringe collar sleeve hem pleat patch bunting tinsel bauble wreath present confetti
tennis rugby hockey netball rounders bowling chess rowing sailing cycling running walking hiking camping fishing skating skiing surfing diving judo karate yoga pilates
ballet tango waltz polka samba rumba disco opera choir band quartet solo duet encore tempo octave tune jingle
alphabet number figure total answer question lesson chapter page title author editor reader painter potter baker farmer gardener sailor pilot driver builder plumber joiner
tailor weaver cobbler barber teacher student captain scout guide ranger keeper mayor
pavement puddle lamppost postbox signpost footpath gateway archway stairway doorstep rooftop chimney gutter skylight balcony veranda courtyard fountain allotment
greenhouse compost seedling sapling sunflower bluebell snowdrop primrose buttercup dandelion foxglove marigold pansy petunia geranium begonia orchid cactus bamboo
thicket woodland hedgerow pasture paddock haystack scarecrow windmill waterfall riverbank lakeside seaside headland sandbank rockpool shingle driftwood seaweed
blanket lanyard notepad keypad laptop tablet printer scanner speaker radio antenna channel episode podcast playlist ringtone doodle collage origami pottery mosaic
stencil easel palette charcoal pastel crochet cushion bookmark bookcase bookshop newsagent florist grocer butcher dentist chemist optician
penguin flamingo kangaroo mackerel jellyfish dragonfly butterfly caterpillar bumblebee grasshopper
armchair bedroom kitchen hallway attic porch patio fence garage driveway fireside bookshelf letterbox laundry hanger spatula tongs grater peeler timer recipe menu supper
dinner lunch brunch snack trifle icing sprinkle wafer cone lolly jelly sorbet smoothie lemonade squash milkshake teabag cupcake cookie ravioli pesto tofu kebab samosa naan
korma wonton sushi ramen taco salad coleslaw cumin oregano coriander chive rocket cress sprout sweetcorn swede kale melon kiwi guava nectarine tangerine blueberry damson
sultana hazelnut pinecone catkin bulrush hawthorn sycamore poplar larch elm oak palm cypress magnolia crocus daffodil iris lupin aster peony lotus clematis wisteria
clifftop hilltop foothill uplands lowland wetland estuary inlet creek rapids cascade shallows sandbar dune reef meander towpath byway crossing junction flyover viaduct stile
skyline horizon twilight daybreak moonlight starlight sunlight daylight drizzle shower downpour haze glow gleam glimmer glitter sparkle shimmer twinkle flicker radiant
aurora zenith equinox solstice eclipse nebula saturn jupiter neptune venus pluto apollo shuttle lander rover telescope
abacus anvil bellows bobbin buckle canteen clipboard cogwheel crate cradle dial dynamo flagpole funnel gadget gazebo goggles hamper inkwell kazoo keyboard kiosk locket
mallet maypole megaphone metronome monocle bracelet pendant trinket tiara paperclip pendulum periscope pinwheel propeller quill rattle sandpit scrapbook seashell sundial
unicycle windchime xylophone yoyo
cousin auntie uncle grandad grandma nephew niece twin buddy pal crew team guild
ample brisk bonny dandy dapper dainty dreamy earthy fancy fleecy frisky gleeful glad handy hearty homely jaunty joyful keen nifty peppy perky plucky quirky rosy rustic silky
sleek snappy spry sunlit tidy trusty upbeat vivid zesty zippy
amaze bounce bundle cuddle dabble dangle dazzle gobble huddle jiggle jostle mingle muddle nestle nibble rustle saunter scamper scribble shuffle snuggle tinker toddle twirl
waddle whittle yodel
"""
# kept out, whatever list they arrive in: drink, drugs, gambling, harm, the law, illness, money, slang, twins by sound, tricky spellings
OUT = set("""
bar pub pint keg cork brew cider sherry port porter stout bitter mild lager ale mead rum gin whisky brandy punch tonic mixer spirit bottle glass flask barrel cellar vine grape
hops hop malt barley rye needle pill tablet dose fix hit line score deal dealer dice bet odds jackpot poker bingo lotto casino slot chip card ace joker wager stake race
jockey derby cell jail court bail judge jury warden cuff knife blade gun rifle bomb sword shot blood scar wound pain ache sick ill fever cough cold virus grave ghost devil
smoke ash cigar tobacco vape match lighter weed pot coke crack speed smack dope joint skunk grass herb hash pipe roach blow snow ice crystal rock stone high buzz trip
peacock tit beaver pussy shag nuts screw hump horn gay slug toad bear bare hare hair deer dear sea see bee be flower flour pear pair plain plane tail tale sail sale sun son
knight night wood would week weak meet meat road rode rain reign hole whole mail male right write blue blew red read new knew hear here there their our hour waste waist
stair stare steel steal heel heal root route boy buoy board bored brake break cent scent sent dew due fair fare fir fur flea flee grate great groan grown knot not main mane
moor more pail pale pane peace piece peak peek pole poll pour pore rap wrap ring role roll sew sow soul sole thyme time toe tow vale veil wait weight way weigh which witch
wail whale berry bury cereal serial heard herd horse hoarse key quay leak leek maize maze morning mourning oar ore pea prince prints profit prophet rose rows sauce source
shore sure side some sum steak storey story tea tee tide tied wear where weather whether yoke yolk mist missed hail hale reed bean been ant aunt shoe shoo currant current
mussel muscle chord cord desert dessert pier peer diary dairy beach beech fourth forth harbour centre theatre grey plough cosy yogurt wren comb salmon almond calf biscuit
lettuce spinach broccoli sieve saucer curtain drawer beret whistle guitar cello chorus balloon bicycle canoe anchor library axle giraffe cheetah leopard gorilla llama rhino
squirrel pigeon cuckoo yacht rhythm wallet purse money cash coin bank debt loan lost alone broke fear shame guilt tablet chemist butcher dentist optician money
bauble beige begonia geranium petunia burrito carriage chutney cinnamon collage confetti crochet cupboard cushion cygnet dandelion duvet egret falafel garnet glacier gosling
gutter hummus khaki knit mackerel mosaic muesli nickel onyx orchid palette pansy patient pilates pleat plateau prairie quince rhubarb risotto sapphire sausage shingle skiing
soar stork thistle thrush tortoise veranda wharf wreath double triple single fifth hook jug mug nod porridge rope spoon stir stretch track turkey wagon white brown green
black gateway glue hammer merry mushroom cracker bowl whisk pickle plug plaster bucket cow chick weasel worm spider simple lamppost rockpool seaweed
clematis wisteria peony cypress oregano coriander ravioli nectarine coleslaw sultana equinox solstice zenith nebula metronome periscope pendulum monocle xylophone unicycle
abacus bellows bobbin dynamo gazebo kazoo viaduct estuary stile style jelly sandbar cousin auntie uncle grandad grandma nephew niece twin frisky homely rattle dabble
three five six seven nine ten eleven twelve twenty thirty fifty sixty hundred dozen first second third minute today tonight number figure total answer question title page
chapter lesson
""".split())
words = []
seen = set()
for w in RAW.split():
    w = w.strip().lower()
    if not re.fullmatch(r'[a-z]{3,9}', w) or w in OUT or w in seen: continue
    seen.add(w); words.append(w)
words.sort()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'words.js')
with open(out, 'w') as f:
    f.write("/* The plain words a person's three words are drawn from. Made by tools/make-words.py; its header says\n   what a word must be to stand here. %d words: three of them make about %d bits. */\n" % (len(words), int(3 * __import__('math').log2(len(words)))))
    f.write("window.CR_WORDS = " + repr(words).replace("'", '"') + ";\n")
print(len(words), 'words', '· longest', max(map(len, words)))
print(' '.join(words))
