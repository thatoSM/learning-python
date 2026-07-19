# Thato — AI Engineering Roadmap: MASTER PLAN

**This is my single source of truth.** If I lose access to Claude (temporarily or otherwise), I open this file and keep going. Nothing here depends on any one tool or any one AI. Everything I need to not stall is in this document.

- **Owner:** Thato — Year 2 BSc IT (Software Engineering), Eduvos, South Africa (Johannesburg)
- **Last recorded position:** Day 32 — LeetCode #88 SOLVED (9 problems total)
   - **CURRENT DAY:** 32
   - **File last updated:** 19 July 2026

---

## 0. HOW TO USE THIS FILE (read first)

1. **Find today's day number.** Count consecutive days since Day 1, or check my roadmap notes. Write it at the top of this file.
2. **Locate myself** in the month-by-month plan (Section 8). That tells me what phase I'm in and what's next.
3. **Check the weekly rhythm** (Section 4) for today's focus (Mon/Wed = LeetCode, Tue/Thu = study, Fri = explore, Sat = build, Sun = rest).
4. **Do the work** for that day, following the protocols in Sections 5–7.
5. **End the session** by updating the current day, the daily log, and writing tomorrow's opener (Section 11).

**If I have NO AI at all:** I can still execute. The learning protocol, git workflow, LeetCode format, and month plan are all spelled out below. I coach myself: attempt first, struggle, then look up ONE hint — never paste a full solution I didn't write.

**If I have a DIFFERENT AI (ChatGPT, Gemini, local model, etc.):** paste the "Resume Prompt" in Section 12 to bootstrap it into my coach in one message.

---

## 1. THE GOAL (one paragraph)

Execute a 24-month structured plan to graduate as a competitive **AI Engineer** with production AI systems, 2 AWS certifications, and a live SaaS product (Study Companion). Stay in current BSc IT (no switch to Data Science). **Primary specialisation: AI Engineering. Secondary: Cloud/DevOps.**

**Graduation pitch:** *"I'm an AI engineer who builds and deploys production AI systems — here are 5 projects, 2 cloud certifications, and a live SaaS product to prove it."*

**Near-term target:** first developer role in South Africa (SA-first junior SWE / AI engineer).
**Longer-term (months 18–24+):** Field Deployed Engineer (FDE) positioning, international remote. FDE is a realistic Year-2-to-4 target, NOT a fresh-graduate first job.

---
## 1.5 NORTH STAR — Beyond the Plan (added Day 31+, July 2026)

**The 24-month plan is a floor, not a ceiling.** Its goals (Study Companion,
AWS certs, first dev role) are checkpoints, not the destination. What I'm
actually building is the general capability to create things bigger and
better than I can currently imagine — my own products, companies, systems
that don't exist yet.

**Why the plan still rules day-to-day:** ambition without foundations
produces nothing shippable. Every locked decision and every rep in this
plan compounds into the exact skillset that makes "greater than I could
imagine" possible: idea → architecture → working code → deployed product
→ real users. The discipline IS the unlock.

**Rules for big ideas:**
1. When a big idea strikes, WRITE IT DOWN here (Idea Vault below) —
   never act on it mid-stride.
2. Big ideas get evaluated at monthly retrospectives only, with the
   structured-justification process for roadmap changes.
3. "Beyond the plan" never means "instead of the plan." Skipping
   foundations to chase an idea breaks the compounding.
4. After graduation + first role, this vault becomes the source for
   what I build next.

**Idea Vault:**
- SA Universal Translator (deferred SaaS — already logged)
- AI CV Reviewer for SA graduates (deferred SaaS — already logged)
- SmallBiz AI via WhatsApp (deferred SaaS — already logged)
- [new ideas go here, one line each, with date]

## 2. WHO I AM / CONSTRAINTS

- Year 2 BSc IT (Software Engineering), Eduvos, SA. Lives at home with family (Johannesburg).
- Grades deliberately in 65–75% range — leaves room for self-directed projects.
- **~1–2 hours/day** available outside coursework. **~10 hours/week total.**
- **R500/month** discretionary budget.
- Decent laptop + desktop PC, stable dev setup. Windows + PowerShell + VS Code.
- Plays Fortnite competitively (hobby). Family time is a real value. **Sunday rest is non-negotiable.**

**How I work best:**
- Detailed step-by-step instructions like it's my first time doing the task.
- Honest pushback over agreement. I catch my own mistakes when I re-read code carefully.
- I ask sharp meta-questions about learning and engineering practice.

---

## 3. REPO PATHS & STRUCTURE

**Main repo:** `learning-python` — hosted on GitHub, local at `~/projects/learning-python`

Current structure (Day 31):
```
learning-python/
  calculator/            calculator.py
  docs/                  LEARNING_LOG.md  (+ this MASTER_PLAN.md — see below)
  leetcode/              001_two_sum.py ... 344_reverse_string.py
  practice/              dictionaries_basics.py, list_comprehensions.py, retest_125_...
  rock_paper_scissors/   rock_paper_scissors.py
  task_manager/          task_manager.py, tasks.json
  hello.py
  README.md
  .gitignore
```

**Where to keep THIS file so it never gets lost:**
1. **Primary:** commit it to the repo at `~/projects/learning-python/docs/MASTER_PLAN.md` (version-controlled, on GitHub — survives laptop loss).
2. **Backup 1:** email it to myself (tsmofokeng18@gmail.com) after each major update.
3. **Backup 2:** copy into Google Drive / OneDrive.
Three copies in three places = it's effectively impossible to lose.

**Repo tooling:** `npx repomix@latest` packs the whole repo into one XML file for pasting into any AI as context. `repomix-output.xml` and `tasks.json` are generated/user-data — **do NOT track them in git** (they're in `.gitignore`).

**Planned repo splits/additions (future):**
- Move `leetcode/` into its own repo ~month 3–4.
- Project repos created as I reach them: SA Services Status Tracker (months 4–8), Study Companion (months 13–18). Docker files, GitHub Actions workflows, and AWS deploy configs live in THOSE repos, not here.

---

## 4. WEEKLY RHYTHM (LOCKED — don't change)

| Day | Focus | Hours |
|---|---|---|
| Monday | LeetCode | 1.5 |
| Tuesday | Study (fast.ai / Python concept) | 1.5 |
| Wednesday | LeetCode | 1.5 |
| Thursday | Study day (sometimes retests) | 1.5 |
| Friday | Explore (light reading, tech awareness) | 1.5 |
| Saturday | Build session (project work) | 2.5 |
| Sunday | Full rest (no coding, tutorials, or GitHub) | 0 |

**Total ~10 hours/week** (down from initial 15, for sustainability).

**Golden rule:** Never miss two days in a row. Rest days are part of the plan, not a broken streak. Sunday rest is non-negotiable infrastructure.

---

## 5. LEARNING PROTOCOL (CRITICAL — LOCKED Day 21)

**I am coaching myself to build PRODUCTION memory, not recognition memory.** Reading code builds recognition; writing code builds production. The whole point of 24 months is converting recognition into production memory so I pass real interviews and ship real code under pressure.

**The protocol for LeetCode and project code:**
1. Take the problem only — no pattern hints, no skeleton up front.
2. Attempt **20–30 minutes** producing SOMETHING. Partial, brute force, even garbage all count. Attempting matters more than succeeding.
3. Only then look for **ONE small hint** or a direction fix — not the full solution.
4. **Three days later, re-test the problem cold** — no peeking. If I fail, rebuild structurally, then re-test again later.

**Never (even when tempted / frustrated):**
- Copy a full working solution and pass it off as mine.
- Use so many hints that filling the blanks isn't real thinking.
- Skip the attempt phase to "save time."
- Submit suspiciously clean code (idiomatic beyond my level, concepts I haven't covered). If I'm about to, stop and ask myself: *"Did I actually write this?"* Honesty is the whole system.

**When genuinely stuck on a NEW concept:** a primer + a skeleton with blanks is fine — but the blanks must require real thinking. "Fill in this single value" is dictation, not learning. Good model = the Day 25 rebuild of #125: split into `clean_string` and `isPalindrome`, wrote each with structural hints, ran separately.

---

## 6. WORKFLOW STANDARDS (LOCKED)

### Git
- **Always run `git status` before any `git add`.**
- Folder-level adds (`git add practice/`) fine when status confirms only intended files changed.
- Specific adds (`git add path/file.py`) for surgical control.
- **NEVER use `git add .`** — too dangerous.
- Around month 4–5, introduce `git add -p` for chunk-level review.
- **Never rewrite git history** (no destructive history commands).
- `git mv` does NOT auto-create destination folders — run `mkdir` first (hard-won lesson).
- Edit `.gitignore` directly in VS Code on Windows (avoids PowerShell encoding issues).

### Commit messages (LOCKED)
- **NO "Day X" or dates in commit messages or code docstrings.**
- Format: `"Solve LeetCode #N - Problem Name (pattern used)"` or `"Add/Refactor [feature] - [what changed]"`.
- Day numbers/dates ONLY belong in: roadmap doc, weekly summaries, personal notes.

### LeetCode
- Use **exact LeetCode function/parameter names** (e.g. `isPalindrome`, `containsDuplicate`) so local code pastes straight into the submit window.
- Reword problem statements in my own words in docstrings — never copy verbatim (copyright + better interview signal).
- 3-digit filename prefix: `001_two_sum.py`, `088_merge_sorted_array.py`.
- Re-tests live in `practice/`, not `leetcode/`. Cold attempt, no scroll-back. Failures are information, not failure.

### Docstring format for LeetCode files
```python
"""
LeetCode #N - Problem Name (Difficulty)

Problem (in my words):
    [Reworded in 2-4 sentences]

Examples:
    input1   ->   output1
    input2   ->   output2

Constraints:
    [Brief]

Approach:
    [How solved, 2-4 sentences, mentioning the pattern]

What I learned:
    - [Bullet]
    - [Bullet]
    - [Bullet]

Pattern: [algorithmic pattern]
Time complexity: O(?) - [why]
Space complexity: O(?) - [why]
"""
```

### Incremental development habit
Write 5–10 lines → save (Ctrl+S) → run → check output → continue. **Don't write 50 lines then run once.** Two seconds of saving/running buys back hours of debugging. Non-negotiable since Day 23.

---

## 7. LOCKED DECISIONS (don't re-litigate)

**Strategic**
1. Stay in BSc IT — no switch to Data Science.
2. AI Engineering primary, Cloud/DevOps secondary.
3. Honours deferred — only if a specific opportunity requires it.
4. 2 AWS certs — Cloud Practitioner (month 6–8), Solutions Architect Associate (month 13–18).
5. ZATech Slack deferred until ~month 2–3 (once GitHub has 5–7 projects + 30+ commits). Use `invite@zatech.co.za` with honest student framing when ready.

**Tech stack — Year 1 (locked)**
- Python primary, JS/TS secondary
- FastAPI backends · Next.js + React + Tailwind frontends
- PostgreSQL primary DB · Redis caching from month 8
- Neo4j basic–intermediate by graduation (Eduvos DB module → Study Companion)
- ChromaDB / Pinecone for vectors · Anthropic API primary LLM
- Docker from month 4–5 · GitHub Actions CI/CD from month 5–7 · Kubernetes intermediate month 10–12+

**AI coding tools (intentionally delayed):** Claude for explanations month 2 · code review month 3 · GitHub Copilot month 4 (Student Pack) · Cursor month 5–6 · Claude Code month 6+.

**Flagship — Eduvos Study Companion (months 13–18):** framed as an **LLMOps showcase**, not "an AI study app." Emphasise RAG with citation grounding, semantic answer evaluation, hallucination detection, fine-tuned domain model, prompt versioning, production observability. Locked features: AI tutor with RAG, spaced repetition (SM-2), daily push alerts with active-recall grading, full material reading mode, multimodal teaching (docs/video/image), voice teachers in any language (Whisper + ElevenLabs), static avatar + voice at launch, hidden-tabs progressive-disclosure UX, past papers archive, study group finder (Neo4j), textbook marketplace, tutor matching, exam tracker, real-time collaborative sessions (month 17, Yjs/Liveblocks), AI evaluation system (month 14–15), fine-tuned small model on SA course materials (month 16–17), AI agent for past-paper search + summarisation + question generation (month 11–12).

**Other projects:**
- SA Services Status Tracker (months 4–8): electricity, water, internet/mobile, transport, fuel, banking, municipal outages. Stack: FastAPI + PostgreSQL + Redis + Next.js + Leaflet/OpenStreetMap. Primary: web scraping (BeautifulSoup + Playwright + schedule). Backup: EskomSePush free tier.
- Agentic Research Synthesis (month 9): searches Scholar/arXiv, reads papers, finds contradictions, produces cited synthesis with error recovery.
- Creative web dev (added): GSAP, Framer Motion, Lenis, Three.js/R3F, SVG/Lottie. Month 3 intro, month 10 deep dive. Portfolio differentiator, not a career specialisation.

**Deferred SaaS (post-graduation):** SA Universal Translator · AI CV Reviewer for SA graduates · SmallBiz AI via WhatsApp.

**2035 futureproofing:** AI evaluation system (month 14–15) · monthly AI safety reading from month 12 · design AI features as multi-step workflows, not single prompts.

---

## 8. MONTH-BY-MONTH PLAN (for "I'm on Day X" navigation)

- **Month 1 (Days 1–30):** Foundation. Python fluency, Git, first projects, LeetCode rhythm. End: 5–10 LeetCode, calculator/RPS/task manager shipped, fast.ai L1–4 watched.
- **Month 2 (Days 31–60):** Python depth. Claude as code explainer ~Week 6–7. CLI Task Manager done. Weather CLI (first API). 15–25 LeetCode. fast.ai L5–6.
- **Month 3 (Days 61–90):** HTML/CSS/JS, Portfolio v1, deploy to Vercel. Claude as code reviewer. GSAP basics half-Saturday. fast.ai in Colab. 30–40 LeetCode.
- **Month 4 (Days 91–120):** GitHub Copilot. FastAPI fundamentals. Web scraping (BeautifulSoup + Playwright). PostgreSQL basics. Docker intro. Web Scraper + FastAPI Weather API. Start SA Services Tracker design.
- **Month 5 (Days 121–150):** Cursor intro. PostgreSQL deep dive. Neo4j basics start (Eduvos DB parallel). CI/CD with GitHub Actions. SA Services Tracker active build. 50–60 LeetCode.
- **Month 6 (Days 151–180):** Anthropic API integration. First AI chatbot. Prompt engineering. Neo4j continued. Begin AWS Cloud Practitioner study. Monthly Latent Space reading starts. Deploy SA Services Tracker v1.
- **Month 7 (Days 181–210):** Take AWS Cloud Practitioner exam. RAG fundamentals. Vector databases. Embeddings. AI Study Assistant prototype (first RAG).
- **Month 8 (Days 211–240):** Redis. Webhooks, WebSockets. JWT auth, OAuth2. OWASP Top 10. SA Services Tracker v2 with caching, auth, user accounts.
- **Month 9 (Days 241–270):** Agentic Research Synthesis project. HuggingFace transformers. First 2–3 blog posts. 80+ LeetCode, Mediums comfortable.
- **Month 10 (Days 271–300):** Portfolio v2 in Next.js + Tailwind. Creative web dev deep dive (4–6 Saturdays). First OSS PRs. Kubernetes concepts. GraphQL basics.
- **Month 11 (Days 301–330):** AI agents deep dive (tool use, function calling, multi-step). MCP exposure. Start Study Companion architecture. Simple AI agent project.
- **Month 12 (Days 331–365):** Year 1 retrospective. Monthly AI safety reading starts. Study Companion agent prototype.
- **Month 13 (Days 366–395):** Study Companion foundation: Next.js + FastAPI + Postgres + Redis + ChromaDB. Auth + billing. Core data models. Neo4j integration. Begin AWS SAA study.
- **Month 14 (Days 396–425):** Material upload + RAG pipeline. AI tutor with citations. Daily push alerts. Active recall (SM-2). AI evaluation system starts. Add cost tracking (log token cost per feature, surface cost-per-user).
- **Month 15 (Days 426–455):** Hidden tabs UX. Material reading mode. Past papers archive. Exam tracker. First real Eduvos users. Continue AWS SAA.
- **Month 16 (Days 456–485):** Voice input (Whisper). Voice output (ElevenLabs). Video teaching. Image teaching (multimodal vision). Voice welcome on app open.
- **Month 17 (Days 486–515):** Fine-tune small model on SA course materials. A/B test vs base. Real-time collaborative sessions. Textbook marketplace MVP. Tutor matching MVP. Production monitoring.
- **Month 18 (Days 516–545):** Take AWS SAA exam. Study Companion public launch. Payments live. Post-launch iteration.
- **Month 19 (Days 546–575):** Differentiator project (AI-engineering-flavored): eval framework as a library OR RAG blog series OR significant OSS.
- **Month 20 (Days 576–605):** Interview prep. System design fundamentals. STAR stories (5–7). Mock interviews. CV for SA + international. Internship search if not yet hired.
- **Month 21 (Days 606–635):** First job applications. LinkedIn + OfferZen. ZATech. International remote in parallel.
- **Month 22 (Days 636–665):** Interview cycles. Salary research + negotiation.
- **Month 23 (Days 666–695):** Offer evaluation. Sign contract.
- **Month 24 (Days 696–720):** Graduation. Onboarding into first role.

---

## 9. CURRENT STATUS (last recorded — Day 31)

- **30 consecutive days** of structured work completed.
- **23 GitHub commits** on `learning-python`.
- **9 LeetCode solved:** #1, #9, #20, #344, #242, #125, #217, #136, #88 (+ #125 retest passed Day 25).
   - **Next re-test:** #88 cold re-test ~Day 35 (in practice/). Stretch goal: solve WITHOUT .sort() — three-pointer merge from the back.
- **4 projects shipped:** Calculator v2, CLI Task Manager, Rock Paper Scissors v3, LeetCode solutions repo.
- **fast.ai L1–4 watched** (top-down, no code-along yet).

**LeetCode patterns done (9 of ~15):** arrays+nested loops (#1), string manipulation (#9, #125), stacks (#20), two pointers (#344, #125), dictionary counting (#242), hash set membership (#217), hash set pair cancellation (#136). In progress: two-array index work (#88).
**Still to cover at Easy:** sliding window, binary search, linked lists, recursion basics, trees DFS/BFS, DP intro, greedy.

**Foundation projects: 4 of 7 shipped.** Remaining: Password Generator (#3), Weather CLI (#5, first API — month 2), Portfolio Website v1 (#7, month 3).

---

## 10. IMMEDIATE NEXT ACTIONS (do these first when I return)

1. **#88 DONE.** Cold re-test ~Day 35 in practice/. Stretch: no .sort(), three pointers from the back.
2. **Three days after solving #88, cold re-test it** in `practice/`.
3. **Enter Month 2 depth:** plan the Weather CLI (my first API call) for an upcoming Saturday build.
4. **~Week 6–7:** start using Claude (or any AI) as a *code explainer* — explanations only, still no ghost-writing.
5. **Watch fast.ai Lesson 5** on a study day.
6. **When repo hits 5–7 projects + 30+ commits (~month 2–3):** join ZATech Slack via `invite@zatech.co.za`.

**Pending deep session (was flagged for Day 33): 2026 SA market recalibration.** Apply these adjustments:
1. Lower SA salary expectation: R30–55K → **R20–35K** realistic for first job.
2. Pull internship search forward: now active in **months 18–20**.
3. Start international remote prep now, not 2–3 years out.
4. Strengthen the differentiator project (AI-engineering-flavored, not generic).
5. More emphasis on real client work in Month 9.
6. Bump blog target from 12 to **15–20**.
*Not cutting:* AI Engineering specialisation, Cloud/DevOps secondary, Study Companion as LLMOps showcase, AWS certs, 24-month timeline.

---

## 11. SESSION-END RITUAL (do every working day)

At the end of each session, update this file:
1. Update **CURRENT DAY** at the top.
2. Add a line to my daily log / LEARNING_LOG.md (what I did today).
3. Write **tomorrow's opener** — a short paste-ready block:
   ```
   Day [N+1] — [weekday, focus per rhythm]
   Just finished: [today's work]
   Next up: [tomorrow's task]
   Suggested ask: [what to request from my coach/AI]
   ```
4. **Every Sunday (or Monday morning):** write a Week N summary (period, status in/out, daily log, new Python concepts, LeetCode patterns, decisions/locks, portfolio status, honest process notes, next-week preview). Paste it into my roadmap doc.

---

## 12. RESUME PROMPT (paste into ANY AI to rebuild my coach)

> You are my AI engineering coach. I'm Thato, a Year 2 BSc IT student at Eduvos in South Africa, executing a 24-month structured plan to become a competitive AI engineer (primary: AI Engineering; secondary: Cloud/DevOps). I'm on Day ___ of 720. I work ~10 hours/week on a fixed rhythm: Mon/Wed LeetCode, Tue/Thu study, Fri explore, Sat build, Sun rest. 
>
> **Critical coaching rule (never break):** You are a COACH, not a ghostwriter. Give me the problem only. I attempt 20–30 minutes first. Then give me ONE small hint — never a full solution I can copy. Three days later I re-test cold. If I submit suspiciously clean code, challenge me and ask if I wrote it myself.
>
> Give detailed step-by-step instructions like it's my first time. Push back honestly instead of just agreeing. Use exact LeetCode function names so my code pastes straight into the submit window. No "Day X" or dates in commit messages or docstrings. I'll paste my full plan and current repo next — read it, locate me in the month-by-month plan, then coach today's work.

Then paste the relevant sections of this file (and optionally run `npx repomix@latest` and paste `repomix-output.xml` so the AI sees my actual code).

---

## 13. THE CORE TRUTH (don't lose this)

The biggest variable in my success is not which AI is helping, not which problem I'm solving, and not which tool I'm using. **It's whether I keep showing up. Daily. For 720 days.**

The plan is sound. The protocol works. Stay honest. Attempt before looking. Celebrate small wins. Protect the rest days. Trust the compounding.

*If Claude ever disappears mid-journey, nothing above changes. I open this file and take the next step.*
