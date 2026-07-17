# learning-python

My Python foundation work on the road to becoming an AI engineer.

I'm a Year 2 BSc IT (Software Engineering) student at Eduvos, South Africa, working through a structured, long-term plan to build production AI systems. This repository holds the **Year 1 foundations**: core Python fluency, algorithmic problem solving, and small projects. It's a working journal of deliberate practice, not a polished product — the goal is visible, honest progress over time.

For a session-by-session record of the whole journey (including study and video days, not just code), see [`LEARNING_LOG.md`](LEARNING_LOG.md).

---

## Repository structure

```
learning-python/
├── leetcode/          # Algorithm solutions, one file per problem
├── practice/          # Concept drills and cold re-tests
├── calculator.py      # Project: calculator with functions, error handling, history
├── rock_paper_scissors/
│   └── rock_paper_scissors.py   # Project: RPS with input validation
├── task_manager/      # Project: CLI task manager (classes, JSON, file I/O)
├── hello.py
├── LEARNING_LOG.md    # Chronological journal of every session
└── README.md
```

---

## What's inside

### LeetCode (`leetcode/`)
Each solution is a standalone file following a fixed convention:

- **Exact LeetCode signatures** — `class Solution` with the real method name (e.g. `isPalindrome`, `containsDuplicate`) so a file pastes straight into the submit window.
- **Problem restated in my own words** in the docstring — never copied verbatim from LeetCode.
- **Documented reasoning** — approach, what I learned, the algorithmic pattern, and time/space complexity.
- **3-digit filename prefix** for ordering: `001_two_sum.py`.

Patterns covered so far: arrays and nested loops, string manipulation, stacks, two pointers, dictionary counting, and hash-set membership.

### Projects
- **Calculator** — functions, error handling, calculation history, power operation.
- **Rock Paper Scissors** — game loop with input validation.
- **CLI Task Manager** — classes, `__init__`/`self`/methods, JSON persistence, file I/O.

### Practice (`practice/`)
Concept deep-dives (list comprehensions, dictionary basics) and **cold re-tests** — re-solving past problems from scratch a few days later to convert recognition into real recall.

---

## Conventions I follow

- **Attempt first, hints second.** I solve problems myself before looking anything up; documented reasoning comes after a genuine attempt.
- **Save → run → check, in small steps.** Write a few lines, save, run, verify output — rather than writing a lot and debugging blind.
- **Clean git history.** `git status` before every add, no `git add .`, descriptive commit messages, no history rewrites.
- **Own words.** Problem statements and notes are always reworded, never pasted.

---

## Progress snapshot

- **9 LeetCode problems** solved across 7 core easy patterns
- **3 mini-projects** shipped (calculator, RPS, task manager)
- Foundations in place: functions, classes, file I/O, JSON, comprehensions, sets, error handling

_This snapshot is updated as the work grows. See [`LEARNING_LOG.md`](LEARNING_LOG.md) for the full timeline._
