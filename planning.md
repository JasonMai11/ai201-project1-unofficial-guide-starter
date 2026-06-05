# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
My domain is how to play / climb the ranks of Team Fight Tactics (TFT). 
TFT doesn't really place you in a tutorial, instead they have a dedication YouTube video on how to play.
This knowledge is hard to find since TFT could only introduce the basics on how TFT functions but not
how to scale to the end game and secure a place within the top 4 or even better, win 1st place.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
We will need large chunks since information about the basics of TFT typically span over a couple sentences (2-3 sentences)
Lets start with a chunk size of 500
We'll scale up or down depending on our results.

**Overlap:**
We should do an overlap of 100 to get that extra sentence if needed.

**Reasoning:**
TFT basics contains lots of information that could span over a couple sentences to get a point across.
---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
We will start with the suggested Tech Stack Embedding Model 
sentence-transformers (all-MiniLM-L6-V2)

**Top-k:**
We are most likely going to receive 200-250 chunks per query to go over most of the information the guides provide.

**Production tradeoff reflection:**
The trade offs would definitely be costs since we would probably need a large context length to go over many of the guides provided by the sources.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | How much interest will I get if I have 50 gold saved? | You will recieve 5 gold from interest. |
| 2 | Is it better to have my carries placed in the front of the board or back of the board? | It depends, but ranged carries perform better at the bottom of the board. |
| 3 | If I am playing for a 3 cost reroll composition, what level should I be rolling my gold? | Level 7 is the best level to roll your gold since you have the most odds of finding 3-costs. |
| 4 | If I am playing for a fast 9 composition, how much gold should I be saving? | You should be saving 50 gold and using the remaining (while staying above 50 gold) to level to 9. |
| 5 | What item is flexible to put on any unit? | Twisted gloves as they guarantee two random items each round. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. I feel like the information from other guides could contradict each other since people are entitled to their own opinion on how to
progress in the game

2. Some chunks can return false information since some questions can be very vague. Or some questions might not be answered due to missing information from the documents.

3. TFT is a very complex game so answers may seem a little wonky too.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     Claude

     - What you'll give it as input (which sections of this planning.md, which requirements)
     I plan to give it my architecture and my chunking strategy

     - What you expect it to produce
     I expect it to produce my chunking strategy and UI

     - How you'll verify the output matches your spec
     I'll verify the output with my expected answers

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
Ingestion and Chunking has been implemented with Claude.
I tested various chunking strategies (although it was hard to be satisfied since chunks of many sizes seemed ok to me)

**Milestone 4 — Embedding and retrieval:**
Embedding and Retrieval was implemented.
The chunks embedded using the recommended techstack (Sentence-transformers all-miniLM-L6-V2)
Retrieval was implemented and tested using 'python retrieval.py' to run it against my example queries.

**Milestone 5 — Generation and interface:**
