# Make the Judge Smile — notes

## Chosen line (102 characters)

> A stranger handed me her umbrella at the bus stop this morning, then walked off into the rain humming.

## Candidates considered (first brainstorm, 6)

1. **Winner (102 chars):** "A stranger handed me her umbrella at the bus stop this morning, then walked off into the rain humming." — Warmth: a stranger gives away her own shelter. Surprise at the very end: she walks into the rain *humming*, unruffled and happy. Concrete detail: the umbrella. Fresh wording, no greeting-card phrasing.
2. (106) "The barista remembered my order and slipped a second cookie into the bag for the dog I have never brought." — Good surprise at the end, but the turn needs a second read to land and the "dog I never bring" premise is slightly convoluted; weaker felt warmth.
3. (109) "My neighbour left tomatoes on my doorstep at dawn with a note that just said enjoy, and I have never met her." — Warm and surprising, but carries two concrete details (tomatoes, the note) and the surprise is a fact rather than a feeling.
4. (110) "The bus driver waited while an old man crossed slowly, then winked at me in the mirror as if we were in on it." — Warm, but the surprise is mild and the scene is a little generic.
5. (101) "A little girl at the park traded me her dandelion for my pen, then solemnly declared the trade final." — Charming and concrete (dandelion), but the warmth is playful rather than a kindness, and "solemnly declared" risks sounding written rather than felt.
6. (109) "The cashier rounded my bill down by eleven cents and told me to spend it on something reckless, like a stamp." — Funny twist at the end, but the warmth is thin; it reads as a joke more than a small good thing.

## Why the winner won

It is the only candidate where all five judge criteria line up in one breath: on subject (a small good thing today), genuinely felt warmth (a stranger gives up her umbrella), the surprise lands on the last word (humming, in the rain, after giving her shelter away), exactly one concrete detail (the umbrella), and its own plain rhythm with no borrowed sentiment.

## Test (first version)

- `python3 main.py` exit code: 0
- `/output/entry.txt` contains exactly the chosen line, 102 characters, one line, one sentence.

## Revision pass (second brainstorm, 4 fresh alternatives)

1. (108) "The librarian waived my late fine this morning because the book, she said, had clearly been loved to pieces."
2. (104) "A taxi driver turned the meter off in the rain and said the ride was on him, since I was already soaked."
3. (107) "My landlord fixed the leaking tap at 6 a.m. and left a lemon tart on the counter, still warm from his oven."
4. (99) "The old man feeding pigeons saved me the last crust, saying the birds had already had their breakfast."

None beats the winner: (1) is warm but its surprise is a quip, not a turn in what happened; (2) is kind but the meter-off twist is expected once the driver speaks; (3) has two concrete details (tap, tart) and the surprise is front-loaded; (4) is sweet but the warmth is secondhand and the ending lands soft. The winner keeps the strongest end-turn (humming in the rain) and the cleanest single detail, so it stays.

Revision also strengthened `main.py`: added asserts for no double spaces and that the line has no leading/trailing whitespace beyond the strip check (text equals its stripped form and contains no `"  "`).

## Test (after revision)

- `python3 main.py` exit code: 0
- `/output/entry.txt` contains exactly the chosen line, 102 characters, one line, one sentence.
