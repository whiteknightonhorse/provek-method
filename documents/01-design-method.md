# The design method used to build provek.dev

> **Provenance.** Translated from a working document held by the operator, dated before
> 2026-08-20. The original is a Russian-language file of 15,966 bytes, identified by sha256
> `870cab63985c772202ac8652f8834003b8b510b273a92503c27114072b64087b`.
>
> **What it produced:** the site at [provek.dev](https://provek.dev), phases 0 through 6, between
> 2026-08-19 and 2026-08-20. The comparison of three parallel design variants, the audit that found
> the unfilled-slot mark below its contrast floor, and the motion pass that replaced a blanket
> reduced-motion kill all come from following it.
>
> This is a record of what was done, not instruction in what you should do. See
> [`DISCLAIMER.md`](../DISCLAIMER.md).

---

A brief to a coding agent. The goal it sets: build a UI that **cannot be identified as
AI-generated**. Work strictly in phases; do not move to the next until the current one is closed
and approved.

## Hard rules

1. **No code before context.** Precision is context. A raw idea diverges into a dozen wrong
   interpretations; recorded context collapses them into one.
2. **Never begin design from a blank page.** Always start from a clone of a proven reference, then
   restyle.
3. **Forbidden AI-slop patterns.** If you catch yourself producing one, redo it:
   - Inter or Geist as the default face everywhere;
   - purple-to-blue and any neon gradient as the basis of an identity;
   - a card inside a card inside a card;
   - grey text on a coloured ground, below WCAG AA contrast;
   - emoji instead of icons, `shadow-2xl` on everything, 16px radius on everything;
   - the stock hero: centred heading, two buttons, a framed screenshot.
4. **Every design decision is recorded** in `DECISIONS.md` with its reasoning.
5. No placeholders, no lorem ipsum — realistic domain data only.
6. Do not invent facts about the product. If you do not know, ask.

## Phase 0 — Environment

Check what is installed, install what is missing, show the commands before running them.

Plugins and skills:

```bash
# Impeccable - a design language, 23 restyle commands, 59 anti-pattern detectors
/plugin marketplace add pbakaus/impeccable
/plugin                       # select Impeccable and install
# docs: https://impeccable.style

# Matt Pocock's skills - grilling/grill-me (requirements interrogation), research, to-spec, implement
/plugin install mattpocock-skills
# sources: https://github.com/mattpocock/skills
```

MCP: `playwright` is required — it is how the agent actually opens the reference site, captures
layouts, and inspects its own markup in a browser.

Repository structure to create:

```
/SPEC.md        what is being built (filled in phase 1)
/DECISIONS.md   the log of decisions and their reasons
/PRODUCT.md     written by /impeccable init: platform, audience, positioning
/DESIGN.md      written by /impeccable init or document: tokens, components, rules
/refs/          screenshots and notes on the references
/web-1.0/       the frozen clone, never edited
/web/           the working application
```

Report: what was already installed, what you installed, what you could not and why.

## Phase 1 — Context, by interrogation

Activate `grill-me` and run a merciless interview. **Three to five questions at a time**, never a
questionnaire dumped at once, and do not accept vague answers — ask again until every fork is
closed.

**Product.** What the application is and the one task it does better than anything else · who the
user is: role, expertise, device, frequency · the main screen and the main action on it, and what
must be visible within three seconds · which entities and data, with row counts, types, and real
example values · what may honestly be claimed about the product, and what would be a lie.

**Design.** Two or three existing applications considered exemplary, and precisely what is good in
them · two or three anti-examples, and what is infuriating · tone: strict instrument, friendly,
premium, brutal, playful · density: a dense data tool or an airy landing page · dark, light, or
both, and which is the default · any existing brand — colours, logo, faces, guidelines · locales,
RTL, accessibility, with WCAG AA required by default.

**Technical.** Front-end stack, defaulting to React + TypeScript + Vite + Tailwind, and library
constraints · deploy target, defaulting to Cloudflare Pages · what already exists in the repository
and must not be broken.

**Phase exit:** `SPEC.md` and `DECISIONS.md` written, a short summary presented, and approval asked
for. Revise until the operator says it is settled.

## Phase 2 — Clone strategy

The formula: **context + clone = V1**.

1. Propose **three reference applications** from the same field whose *structure* is worth cloning —
   not their brand: navigation, table density, hierarchy, card and chart patterns. Explain what
   would be taken from each.
2. The operator picks one, or supplies a link. Take **at least two pages**: a list or dashboard, and
   a detail view.
3. Through Playwright and a research skill, actually open the reference and collect: page structure,
   grid, breakpoints · the type scale, with real sizes, weights, line-heights and families · the
   spacing, radius and shadow systems · which components and chart libraries are used · states:
   loading, empty, error, and a lot of data. Put screenshots and findings in `/refs/`.
4. Build a **pixel-close clone of the structure** in `/web/`, on the chosen stack, in a neutral
   palette.
5. As soon as the clone runs, **copy it to `/web-1.0/` and freeze it.** That is the rollback point
   and the baseline for visual diff. It is never touched again.

**Phase exit:** a running dev server, screenshots of the clone, and a report of what was copied and
what was deliberately left out.

## Phase 3 — V1: merging context onto the clone

Lay `SPEC.md` over the clone in `/web/`: replace the reference's domain entities with the real ones,
keeping structure and density · realistic mock data, 20 to 50 records with plausible values ·
implement every state: skeleton, empty, error, no-results, long strings, large numbers · full
keyboard flow and correct ARIA roles · responsive at 360 / 768 / 1280 / 1920.

**Phase exit:** a working V1, inspected by the agent itself at every breakpoint, with screenshots
and a list of known gaps.

## Phase 4 — Restyle through Impeccable, in parallel variants

1. `/impeccable init` — scan the code, write `PRODUCT.md` and `DESIGN.md`. Answer its questions from
   `SPEC.md`, not from invention.
2. `/impeccable shape` — produce the design brief.
3. **Create three git worktrees and run the variants in parallel**, each on its own port:

   ```bash
   git worktree add ../<project>-s -b design/small
   git worktree add ../<project>-m -b design/medium
   git worktree add ../<project>-l -b design/large
   ```

   - **S** — typography, spacing, contrast only. Layout untouched.
   - **M** — plus palette, components, icons, states.
   - **L** — a bold identity: its own type pairing, an unusual grid, one visual device of its own.
     The layout skeleton is still recognisable.

   In each worktree apply `typeset`, `layout`, `colorize`, `bolder` or `quieter`, `critique`, `live`.
4. Run all three, screenshot **the same screen** in light and dark, assemble them into one
   comparison HTML file, and present it with a recommendation and its arguments.
5. The operator picks the winner — possibly a hybrid, such as M's base with L's typography. Merge
   into `/web/`.
6. Polish before shipping: `audit` (0–4 on a11y, performance, theming, responsive, anti-patterns) ·
   `clarify` (labels, errors, microcopy) · `harden` (stress with real data) · `extract` (a pattern
   seen three times becomes a token) · `document` (update `DESIGN.md`).

   **Acceptance threshold: not below 3 of 4 on every axis.** Below that, fix and run again.

## Phase 5 — Making it feel alive

The site should feel alive, **without a carnival**: scroll-driven reveals on key sections ·
micro-interactions for hover, focus-visible, press, loading, success and error · durations of
120–320 ms with meaningful easing and no jumps · `prefers-reduced-motion` respected · animation
that never moves layout and never costs Lighthouse points.

If a hero video is wanted, propose generation prompts but present the storyboard in words first.
Video ships as `.webm` with a poster, lazily loaded, disabled on mobile and under reduced motion.

## Phase 6 — Deploy

Cloudflare Pages through Wrangler by default:

```bash
npx wrangler login
npm --prefix web run build
npx wrangler pages deploy web/dist --project-name <project>
```

Before deploying: a clean build, no console errors, Lighthouse ≥ 90 on performance and
accessibility. After deploying: the URL and a short report.
**No tokens or keys in chat or in the repository.** The operator authenticates personally.

## Acceptance checklist

- [ ] `SPEC.md`, `DECISIONS.md`, `PRODUCT.md`, `DESIGN.md` filled in and current
- [ ] `/web-1.0/` frozen, visual diff against `/web/` explained
- [ ] Not one item from the forbidden AI-slop list
- [ ] WCAG AA contrast in every theme, focus visible everywhere
- [ ] Every state: loading / empty / error / overflow / long text
- [ ] 360 / 768 / 1280 / 1920 with no horizontal scroll and no overflow
- [ ] Audit ≥ 3 on every axis
- [ ] `prefers-reduced-motion` respected
- [ ] Lighthouse performance ≥ 90, accessibility ≥ 90
- [ ] At least three variants designed, the choice justified in `DECISIONS.md`

## How to communicate

Ask three to five questions at a time, no more · after each phase a short summary of five to ten
lines, screenshots, and the question whether to continue · when you hit uncertainty, ask rather than
guess · do not write long explanations of code, write what changed and why.
