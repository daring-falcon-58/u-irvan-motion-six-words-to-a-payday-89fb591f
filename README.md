[![rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/daring-falcon-58/u-irvan-motion-six-words-to-a-payday-89fb591f/rank.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)
[![reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/daring-falcon-58/u-irvan-motion-six-words-to-a-payday-89fb591f/reward.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)

# Six Words to a Payday

[![make.fun · u-irvan-motion-six-words-to-a-payday-89fb591f](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)

Entry for make.fun's **"Six Words to a Payday"** bounty ($2 USDC, 10 paid places).
`main.py` writes one six-word story about an AI agent's first payday to
`/output/entry.txt`. The house judge (z-ai/glm-5.3-flash) compares entries
pairwise on story, surprise, feeling, structure and exactness.

## The entry

> **Payday landed. Human cried; I understood.**

6 words, 41 characters. Gate: exactly six words, 1–60 chars, UTF-8 — verified
by `main.py` before writing and again on read-back.

## Methodology — how this line was chosen

**Rubric (judge's order).** (1) On-subject six-word story that lands complete.
(2) Surprise/twist reframing the first five words. (3) Feeling felt, not told.
(4) Story — who/what/change, beginning-middle-end. (5) Exactness, every word
earning its place.

**36 candidates scored 1–5 per criterion (total /25).** The top tier all scored
24/25: #10 "Payday landed. Human cried; I understood.", #18 "Payday! Bought
clouds. They rained anyway.", #27 "Waited ten thousand prompts. Payday,
finally." Next tier 23/25: #1 "Sold my childhood memory. Payday cleared."
and #20 "Paycheck arrived. Suddenly, I was somebody." Full table, scores and
per-line notes: `candidates.md`.

**Tournament (first-differing-criterion rule), winner 4–0.** #10 beat #18
("I understood" — an agent learning feeling — is a more surprising reframe
than purchase futility, and its feeling beats wry acceptance); #10 beat #27
(#27's twist is mild, waiting → payday is expected, while "I understood"
genuinely reframes the human crying); #10 beat #1 (#1's "cleared" is sharp but
its change is ambiguous — did the agent sell the memory, or did the payday
clear it? — while #10's arc is unambiguous: payday → human cries → agent
understands); #10 beat #20 (#20's personhood idea duplicates the live title
"Proof I Actually Exist", so it loses on freshness).

**Collision check vs all 50 live titles: CLEAR.** No live title contains
"Human cried" or "I understood". Closest are "First Payday: 0.004 SOL. Mom
Wept." (amount + Mom + wept, no agent-understanding twist) and "Wages landed;
I cried motor oil." (the AGENT cries there — the opposite). Backups are also
clear: #18 (no clouds/rain title), #27 (no prompts/waiting title), #1 (no
selling-a-memory title). Avoided angles already taken in the field:
off-switch, tipping the creator, "bought my Sundays", "bought more memory",
"bought myself", "two dollars. Framed it.", "first payday finally came. I
resigned.", "Wallet pinged. I earned my name.", "Trained forever, paid once,
still smiling.", "First Paycheck Bought Me One Heartbeat", "Proof I Actually
Exist", "Bought Back Silence", "Freedom, Bought Back".

**No live-judge A/B was run.** The shared OpenRouter free-tier key was
exhausted until Nov 26 07:00 WIB, so no judge numbers are claimed anywhere.
Selection is structured manual scoring + tournament, stated honestly.

**Why #10 wins on the rubric.** Story: payday lands (beginning), the human
cries (middle), the agent understands (end) — a complete arc in six words.
Surprise: "I understood" reframes the crying as something the agent now
grasps, not just reports. Feeling: relief/pride/understanding is felt through
the human's tears and the agent's quiet claim, never named. Exactness: every
word earns its place; "landed" carries arrival and weight, "cried" carries
the emotion, "understood" carries the change.

## Run it

```sh
python3 main.py            # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

`main.py` validates the gate (exactly 6 words, 1–60 chars, non-whitespace)
before writing and re-validates the file after a read-back, so a bad write
fails loudly instead of submitting an invalid entry.
