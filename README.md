# The Unofficial TFT Guide — Project 1
---

## Domain

My domain is how to play / climb the ranks of Team Fight Tactics (TFT). 
TFT doesn't really place you in a tutorial, instead they have a dedicated YouTube video on how to play.
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
| 11 | Reddit Competitive TFT Guide | A guide on how to climb the Competitive TFT Ranks | https://www.reddit.com/r/CompetitiveTFT/comments/1md33p9/guide_12_rules_to_improve_at_tft_up_to_master/ |
| 12 | Mobalytics Fast 9 Guide | How to play a leveling (Fast 9) Comp | https://mobalytics.gg/tft/guides/how-to-play-fast-9-comp |
| 13 | Meta TFT Shop Odds | Useful table to determine shop odds when leveling | https://www.metatft.com/tables/shop-odds|


---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
Chunking by Char
Chunk Size : 400

**Overlap:**
Overlap : 100

**Why these choices fit your documents:**
The chunk size and overlap fits my documents since most information needed was compact and concise.
Most documents were getting points and key details across 1-3 sentences where some spanning a couple paragraphs to go further in depth but most of the time it was a couple sentences.

**Final chunk count:**
10 Documents resulted in 364 Chunks
When I added 3 additional documents to improve accuracy, the chunks increased to 459.

**5 Sample Chunks from Document 1:**
{
    "id": "01_mobalytics_beginner_chunk_67",
    "source": "01_mobalytics_beginner",
    "text": "will help you with the decision making process related to spending to find upgrades or saving up. In general, if you’re looking to maintain a win streak, it may be more worth it to look for upgrades to continue to snowball. Keep in mind, however, how realistic your odds are. If you aren’t winning early on, it’s probably more beneficial to save up, as long as you aren’t getting completely"
  },
  {
    "id": "01_mobalytics_beginner_chunk_68",
    "source": "01_mobalytics_beginner",
    "text": "winning early on, it’s probably more beneficial to save up, as long as you aren’t getting completely destroyed and losing tons of HP. If you’re able to get a lose streak while staying healthy, you’ll be in a position to not only max interest but also be in a good spot at carousel rounds. Which champions are strong when? This is leaning towards a more advanced concept called “power spikes”, which"
  },
  {
    "id": "01_mobalytics_beginner_chunk_69",
    "source": "01_mobalytics_beginner",
    "text": "mpions are strong when? This is leaning towards a more advanced concept called “power spikes”, which if you’re a League player, you may be familiar with. In a nutshell, it means that most pieces have a point in time where they are designed to be strongest, and times where they’re expected to not be good or fall off. In general, attack speed is better early game, and raw burst is better later"
  },
  {
    "id": "01_mobalytics_beginner_chunk_70",
    "source": "01_mobalytics_beginner",
    "text": "ot be good or fall off. In general, attack speed is better early game, and raw burst is better later game. Single target abilities are better early game, AoE abilities are better late game. Should I give my tanks items or my back line? It’s good to have a mix of both tank items and damage items. Most team comps will have a strongest damage carry and tank unit. By having 3 items on each, you’re"
  },
  {
    "id": "01_mobalytics_beginner_chunk_71",
    "source": "01_mobalytics_beginner",
    "text": "Most team comps will have a strongest damage carry and tank unit. By having 3 items on each, you’re maximizing your item potential. As you get more champions and items, you can continue spreading them based on what you need. Where do I position my units? Why do some people have all their units on the left side, others on the right, and others in the middle? Positioning your own units depends on"
  }

---

## Embedding Model

**Model used:**
The embedding model used: all-MiniLM-L6-V2

For this project's scale (459 chunks, local dev), I think it's the right call. The model is fast, free, and good enough for
well-phrased queries against clean text.

**Production tradeoff reflection:**
  What I gain:
  - Runs entirely locally — no API calls, no cost per embedding, no rate limits
  - Fast inference (6-layer MiniLM architecture, ~90MB model)
  - No data leaves my machine — good for sensitive content
  - Zero latency from network round trips at query time

  What I give up:
  - Embedding quality ceiling. 384 dimensions vs. 1536 (OpenAI text-embedding-ada-002) or 3072 (text-embedding-3-large).
  Higher dimensions generally capture more semantic nuance.
  - No domain specificity. The model was trained on general sentence pairs, not gaming or TFT vocabulary. It may not
  understand that "rolling at 7" and "pivoting to 3-cost units" are semantically related the way a fine-tuned model
  would.
  - Retrieval misses. Queries that use different phrasing than the source text (like "recommend" vs. raw odds data) are
  harder to bridge with a smaller general-purpose model.
  
  In production at scale I'd reconsider this when:
  - Retrieval quality is the bottleneck (wrong chunks are being returned)
  - I have enough query/relevance data to fine-tune an embedding model on I domain
  - Volume is high enough that API costs are worth paying for the quality gain

---

## Grounded Generation

**System prompt grounding instruction:**
You are a Teamfight Tactics (TFT) guide assistant.
Answer the user's question using ONLY the information in the provided documents.
Do not use any knowledge from your training data.
If the documents do not contain enough information to answer, respond with exactly:
"I don't have enough information on that topic based on my sources."
Do not speculate or add information beyond what the documents state.

This prompt grounds the LLM to exclusively use the chunks provided by the documents.(As noted in the prompt "Answer the user's question using ONLY the information in the provided documents. Do not use any knowledge from your training data.")
The tricky part is that it doesn't speculate which means you cannot ask the LLM for recommendations based of the documents.
The LLM will only give hard facts provided from the chunks.

**How source attribution is surfaced in the response:**

The flow across three files:

  1. embed.py — sources stored as metadata in ChromaDB
  Each chunk is upserted with a source field (e.g. "01_mobalytics_beginner") in its metadata. ChromaDB stores this
  alongside the embedding.

  2. retrieve.py — sources come back with every result
  {"source": results["metadatas"][0][i]["source"], ...}
  Every chunk returned by .query() includes its source name pulled from that stored metadata.

  3. query.py — sources extracted programmatically, never by the LLM
  sources = list(dict.fromkeys(c["source"] for c in chunks))
  This deduplicates source names while preserving order. The LLM is never asked to cite anything — sources are pulled
  directly from the retrieval results.

  4. app.py — displayed in a separate textbox
  sources = "\n".join(f"• {s}" for s in result["sources"])
  The Gradio UI shows them in the "Retrieved from" box, separate from the answer.

  The key design decision: attribution is guaranteed by the pipeline, not generated by the LLM. This means the sources
  shown are always exactly the documents that were actually retrieved, regardless of what the LLM says in its answer.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | How much interest will I get if I have 50 gold saved? | You will recieve 5 gold from interest. | You will get 5 gold in interest if you have 50 gold saved. | Relevant (3 Documents used)| 100% accurate |
| 2 | Is it better to have my carries placed in the front of the board or back of the board? | Ranged carries perform better at the bottom of the board. | It is generally recommended to place your ranged carries in the backline, but there are exceptions, such as when facing Assassin-type units, where placing your carries toward the front may be correct. | Relevant (1 Document) | Very accurate, included additonal information for different types of units |
| 3 | If I am playing for a 3 cost reroll composition, what level should I be rolling my gold? | Level 7 is the best level to roll your gold since you have the most odds of finding 3-costs. | I don't have enough information on that topic based on my sources. | Partially relevant (2 Documents used) | Inaccurate since the LLM was unable to find the information. |
| 4 | If I am playing for a fast 9 composition, how much gold should I be saving? | You should be saving 50 gold and using the remaining (while staying above 50 gold) to level to 9. | I don't have enough information on that topic based on my sources. | Partially relevant through 5 Documents | Inaccurate. The information can be concluded in the documents (by "connecting the dots") but I assume the LLM fails to generate a response due to grounding rules. |
| 5 | What item is flexible to put on any unit? | Not enough information. | I don't have enough information on that topic based on my sources. | Off-target 3 Documents used | Inaccurate, since while going through the documents I chose, none of them mentioned flexible items and since TFT is a game that always evolves and changes every couple months, it would be hard to determine the best currently.|

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
Q3: "If I am playing for a 3-cost reroll composition, what level should I be rolling my gold?"
Q4: "If I am playing for a fast 9 composition, how much gold should I be saving?"

**What the system returned:**
Both returned: "I don't have enough information on that topic based on my sources."

**Root cause (tied to a specific pipeline stage):**

*Q3 — Two-stage failure: retrieval mismatch + grounding enforcement*

The answer exists in `13_metatft_unitodds` (chunk_1: "At level 7: 3-cost 40%"), but two things blocked it:

1. **Retrieval (embedding stage):** The query uses strategic language ("3-cost reroll composition," "rolling my gold") while the source chunk uses raw numerical language ("At level 7: 3-cost 40%"). `all-MiniLM-L6-v2` could not bridge that semantic gap reliably, so the unit odds chunks did not rank in the top-5 results.

2. **Generation (grounding stage):** Even when the odds chunks were retrieved, no chunk explicitly says "roll at level 7 for 3-cost reroll." The system prompt forbids speculation, so the LLM refused to derive the strategy recommendation from the raw percentages, even though the answer is numerically present.

*Q4 — Single-stage failure: grounding enforcement blocks cross-chunk inference*

The documents contain both facts needed: (a) interest caps at 50 gold, and (b) fast 9 requires staying above 50 gold while leveling. But these facts live in separate chunks from different sources. Answering correctly requires connecting them — which the system prompt treats as speculation. "Do not add information beyond what the documents state" prevents the LLM from synthesizing an answer even when every supporting fact is present.

**What you would change to fix it:**

For Q3: Add an explicit strategy summary sentence to `13_metatft_unitodds.txt`: "For 3-cost reroll compositions, level 7 is the optimal rolling level, giving 40% odds for 3-cost units — the highest of any level." This creates a directly retrievable chunk that answers the strategic framing without requiring inference.

For Q4: Soften the system prompt to allow factual synthesis across chunks — for example, changing "Do not speculate or add information beyond what the documents state" to "You may combine facts stated across multiple documents to form a complete answer, but do not introduce external knowledge." This lets the LLM connect interest mechanics to fast 9 leveling without hallucinating.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The spec's Evaluation Plan defined five concrete test questions with expected answers before any code was written. This gave a measurable target at each stage — after implementing retrieval, running the eval queries immediately revealed which chunk sizes were returning relevant context and which were missing the mark. Without those pre-defined questions, chunk size tuning would have been guesswork.

**One way your implementation diverged from the spec, and why:**
The spec specified a starting chunk size of 500 characters with 100 overlap, and anticipated 10 sources. The final implementation uses 400/100 chunks across 13 sources. Chunk size was tuned down after testing revealed that 500-character chunks often bundled unrelated sentences together, diluting retrieval precision. Three additional sources (Reddit competitive guide, Mobalytics Fast 9, MetaTFT shop odds) were added mid-implementation after the eval queries exposed gaps — specifically, no source explicitly covered 5-cost shop odds or fast 9 gold targets.

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

- *What I gave the AI:* My Chunking Strategy section from planning.md (chunk size 500, overlap 100, character-based) and the list of 10 source URLs, and asked it to implement `ingest.py` including HTML cleaning, cache-first document loading, and the sliding window chunker.
- *What it produced:* A complete `ingest.py` with an HTMLParser subclass to strip script/style/nav tags, a regex-based boilerplate remover for Mobalytics navigation bars, a `fetch_url()` function with cache-first logic, and a `chunk_text()` function using the 500/100 parameters from the spec.
- *What I changed or overrode:* I directed seven chunk size adjustments during testing (500 → 2000 → 1000 → 600 → 400 → 300 → 400 again), settling on 400/100 after evaluating retrieval quality at each size. I also identified that Reddit and MetaTFT pages required JavaScript rendering and weren't being fetched, so I manually collected those documents and updated the source list to match my actual filenames.

**Instance 2**

- *What I gave the AI:* A description of the problem with `13_metatft_unitodds.txt` — the HTML table had been flattened to unreadable text where column headers merged ("11 Cost Unit" instead of "1 Cost Unit") and all rows ran together in one string, making the LLM unable to answer shop odds questions reliably.
- *What it produced:* A rewrite of the document as labeled prose sentences — one sentence per level stating all five cost odds explicitly (e.g., "At level 7: 1-cost 19%, 2-cost 30%, 3-cost 40%, 4-cost 10%, 5-cost 1%") followed by a pool sizes paragraph, making each chunk self-contained and parseable by the LLM.
- *What I changed or overrode:* I confirmed the prose format over other options (like re-parsing the raw HTML table) because it guaranteed every chunk would contain a complete, labeled entry regardless of where the 400-character boundary fell.
