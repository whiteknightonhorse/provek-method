# The skill architecture this project's agents work under

> **Provenance.** Translated from a working document held by the operator, dated before
> 2026-08-20. The original is a Russian-language file of 9,482 bytes, identified by sha256
> `610094546db889ef37908068dad273a852231764fae2cf0d9060a5034024ad1f`.
>
> **What it produced:** the working discipline behind this project — requirements interrogated
> before code, a specification with no code in it, tickets cut vertically rather than by layer, and
> an independent review in a fresh context. `SPEC.md`, `DECISIONS.md` and the sixteen-ticket
> implementation plan in the provek repository were produced this way.
>
> A record of what was done, not instruction in what you should do. See
> [`DISCLAIMER.md`](../DISCLAIMER.md).
>
> The upstream skills are Matt Pocock's and live at
> [github.com/mattpocock/skills](https://github.com/mattpocock/skills). This document is a summary
> of how they were applied here, not a copy of them.

---

## The premise

Use small independent skills rather than one large monolithic framework. Each skill must be
independent, reusable, small, invocable by hand, invocable automatically when the task fits, and
must not require any earlier skill to have run.

The usual order is:

```
idea → grill-me → to-spec → to-tickets → implement → code-review
```

but any of them may be run alone. Do not build one enormous pipeline, and do not create hard
dependencies between stages.

## grill-me — requirements by interrogation

The most-used skill. Instead of writing code, the agent interviews the operator until the
uncertainty is gone. Five rules:

**Relentlessly.** Keep asking until the task is fully understood.

**One branch at a time.** Do not jump between topics. Not «checkout, dashboard, login, profile» at
once — finish checkout entirely, then login, then dashboard.

**One question, one answer**, then the next question.

**Recommend one.** Never ask an empty question. Always propose options: *which is better — Stripe,
LemonSqueezy, or Paddle?*

**Don't act.** Never perform an action without confirmation.

Use it before building any new functionality.

## grill-with-docs — the same interview on an existing project

The same interrogation, but it simultaneously updates `CONTEXT.md`, the ADRs, and the domain model.
Use it when the project already exists.

## to-spec — the discussion becomes a specification

Turns everything discussed into a full specification, without asking anything again: it works from
the context already gathered.

**No code in the specification.** Code goes stale quickly; a specification describes *what to do*,
not how to write it. It contains: problem, solution, user stories, architecture, testing, out of
scope, decisions.

## to-tickets — vertical, never horizontal

Splits the specification into tasks. The important distinction: **do not split by layer.**

Wrong: database, API, frontend. Right: login, registration, checkout, payment, orders.

Each ticket is a complete vertical feature that can be tested the moment it is finished.

## implement — one ticket at a time

Writes code for a single ticket, using `tdd` automatically as it goes.

## tdd

```
write test → run → fail → write code → run → pass → refactor
```

Never write code before the test. It reduces the defect rate.

## code-review — in a fresh context window

After implementation, open a **new context window** and review the code against Martin Fowler's
checklist, using the code-smell vocabulary:

- **Shotgun surgery** — changing one requirement must not require editing twenty files.
- **Feature envy** — logic belongs in the module that owns the data.
- **Data clumps** — parameters that always travel together become a structure.

Review the architecture, not only the errors.

## writing-great-skills

For authoring skills of your own. Minimise text; every word must earn its place. Do not write
"please", "could you", "I appreciate". Write: *interview relentlessly · wait for confirmation ·
suggest options.* Use short professional terms the model already knows rather than long
explanations.

## improve-codebase-architecture — a periodic audit

Analyses git history, finds hot files, runs the deletion test, builds an HTML architecture report,
proposes refactorings, and looks for deep modules. Run it every few days.

## Deep modules

The central idea. A model understands code badly when it has to walk through dozens of functions.
So:

```
a large interface  ✗
    ↓
a small interface
    ↓
large logic behind it
```

The agent should see one entry point rather than fifty functions. This reduces token cost and
improves comprehension of the project.

## The deletion test

For every module found: delete it, run the tests. If nothing broke, delete it for good. If the
tests failed, keep it. It is how dead code gets removed with evidence rather than opinion.

## The principles, restated

1. Every skill is independent.
2. Any skill can be run at any moment.
3. Minimise the volume of instruction inside a skill.
4. Use professional terminology instead of long explanations.
5. Understand the task fully (`grill-me`), then specify (`to-spec`), then cut vertical tickets
   (`to-tickets`), then implement through TDD (`implement` + `tdd`), and close with an independent
   review (`code-review`).
