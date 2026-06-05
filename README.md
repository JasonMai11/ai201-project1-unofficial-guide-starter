# The Unofficial Guide — Project 1
---

## Domain

My domain is how to play / climb the ranks of Team Fight Tactics (TFT). 
TFT doesn't really place you in a tutorial, instead they have a dedication YouTube video on how to play.
This knowledge is hard to find since TFT could only introduce the basics on how TFT functions but not
how to scale to the end game and secure a place within the top 4 or even better, win 1st place.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Mobalytics TFT Beginner Guide | Good broad beginner guide for learning your first TFT match and major game concepts. | https://mobalytics.gg/blog/tft/tft-guide/ |
| 2 | Mobalytics Economy Guide | Covers economy styles like aggressive economy, streaking, and when to spend gold. | https://mobalytics.gg/tft/guides/how-to-manage-your-economy-in-teamfight-tactics-three-strategies |
| 3 | Mobalytics Standard Leveling Strategy | Good for explaining when beginners should level, roll, or save gold. | https://mobalytics.gg/tft/guides/standard-leveling-strategy |
| 4 | Mobalytics TFT Positioning Guide | Covers unit placement, frontline/backline logic, and positioning fundamentals. | https://mobalytics.gg/blog/tft/tft-positioning-guide-how-to-get-the-most-from-your-units/ |
| 5 | Reddit: TFT Fundamentals — Econ and Leveling Guide | Community-written guide focused on economy and leveling from a player perspective. | https://www.reddit.com/r/TeamfightTactics/comments/1gmpr4y/tft_fundamentals_econ_and_leveling_guide_road_to/ |
| 6 | Reddit: Item Economy Fundamentals | Strong source for item decision-making, flexible item use, and avoiding wasted components. | https://www.reddit.com/r/CompetitiveTFT/comments/1hwxtsq/item_economy_fundamentals/ |
| 7 | Reddit: Beginner — How to Learn Positioning? | Good discussion thread for practical beginner questions about positioning. | https://www.reddit.com/r/CompetitiveTFT/comments/14qa1r8/beginner_how_to_learn_positioning/ |
| 8 | MetaTFT Comps | Meta/stat page for team comps, leveling guides, items, augments, and end-game options. | https://www.metatft.com/comps |
| 9 | TFTAcademy Comps Tier List | Curated comp tier list and guide hub from high-level TFT creators. | https://tftacademy.com/tierlist/comps |
| 10 | BunnyMuffins TFT Leveling Guide | Useful outside perspective on when to level and roll, especially for ranked tempo decisions. | https://bunnymuffins.lol/tft-leveling-guide/ |


---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
