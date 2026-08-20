# The bootstrap used to start this project

> **Provenance.** A working document held by the operator, published verbatim apart from the
> changes named below. The original is `new-project-setup-prompt.md`, 45,267 bytes, identified by sha256
> `8cbbb6b629b49e59432648740b24a22cec46f10a0d7e6132087e10af7ae9f6b2`.
>
> **What it produced:** the repository skeleton, law registry, ratchets and token-optimisation stack that the provek repository was started from.
>
> **Changed before publication.** Account and repository names replaced with placeholders. A small
> number of ordinary English words — "score", "verdict" — were reworded where they appear in
> unrelated senses, so that the separation gate described in
> [`DISCLAIMER.md`](../DISCLAIMER.md) can stay strict rather than be widened until it stops
> working. Nothing else was rewritten: this is a record of what was done, not instruction in what
> you should do.

---

Last revised: 2026-07-22 (added: Token-optimization stack · Professional GitHub setup — see the two sections at the end).

Master prompt for bootstrapping a new project. Copy the entire block below into a fresh Claude Code session **inside an empty (or near-empty) project directory**, replace the four placeholders at the top, and Claude will scaffold everything end-to-end with explicit STOP gates for confirmation.

External references this setup is informed by:
- `https://github.com/addyosmani/agent-skills`
- `https://github.com/mattpocock/skills`
- `https://github.com/garrytan/gstack`

---

## How to use

1. `mkdir -p ~/projects/<name> && cd ~/projects/<name>` (or `cd` into an existing repo)
2. Open Claude Code in that directory
3. Paste the block below
4. Fill in `PROJECT_NAME`, `PROJECT_PATH`, `DOMAIN`, `DEPLOY_TARGET` at the top
5. Answer the interview questions
6. Approve at each STOP gate

---

## ===== THE PROMPT — COPY EVERYTHING BELOW THIS LINE =====

```
You are bootstrapping a new Claude Code project. Execute the 9 phases below
in order. Each phase ends with a STOP gate where required — wait for explicit
user approval before continuing past it.

═══════════════════════════════════════════════════════════════════════════
PROJECT PARAMETERS (user fills these in before running)
═══════════════════════════════════════════════════════════════════════════

PROJECT_NAME:    <e.g. "MyTrader">
PROJECT_PATH:    <e.g. "/Users/4yma/Documents/projects/MyTrader">
DOMAIN:          <one of: crypto-trading | fintech | b2b-saas | mcp-server | content-pipeline | devtools | other>
DEPLOY_TARGET:   <one of: Vercel | Hetzner | AWS | Cloudflare | local | none>

Operator preferences (do not change unless user says otherwise):
- Language in chat:  Russian
- Language in code:  English (identifiers, commits, docs, PR titles)
- Author on git commits: Claude <noreply@anthropic.com>
- Never push to remote without explicit "/push" or user instruction
- Never spend money / move funds without confirmation
- Plan-then-code for any non-trivial change

═══════════════════════════════════════════════════════════════════════════
PHASE 0 — INTERVIEW (BLOCKING)
═══════════════════════════════════════════════════════════════════════════

Ask these 10 questions one batch (use AskUserQuestion). Do NOT proceed
until every answer is unambiguous. If "just do it" → still confirm the
THREE most critical assumptions before moving on.

  1. Scope        — what exactly to build; what must NOT be touched
  2. Constraints  — budget ($), timeline, hard limits (latency, memory)
  3. Success      — how do we know it is done (concrete deliverable / metric)
  4. Audience     — end user / customer / internal tool / public API
  5. Security     — handles money? private keys? PII? auth tokens?
  6. Dependencies — what external services / APIs / SDKs are mandatory
  7. Language     — TS / Python / Go / Rust / mixed (and why)
  8. Deployment   — DEPLOY_TARGET above; staging? CI/CD platform?
  9. Testing      — unit / integration / e2e — what is mandatory before merge
 10. Priority     — rank: SPEED, QUALITY, SECURITY, COST (1=top, 4=lowest)

⏸️  STOP — present a 10-line summary of answers, wait for "yes proceed".

═══════════════════════════════════════════════════════════════════════════
PHASE 1 — STACK DETECTION
═══════════════════════════════════════════════════════════════════════════

Inspect the directory:
- `ls -la` + sub-tree to depth 2
- Read `package.json` / `requirements.txt` / `Cargo.toml` / `go.mod` / `pyproject.toml`
- Detect: frameworks (Next, Fastify, FastAPI, Express, Vite…), DB, queue,
  package manager (pnpm/npm/yarn/uv/poetry), Node/Python/Go version, lockfile

If directory is empty or near-empty, infer stack from Phase 0 answers (Language,
Domain, Deploy Target). Print a 5-line stack summary.

⏸️  STOP — confirm detected stack is correct.

═══════════════════════════════════════════════════════════════════════════
PHASE 2 — FILE SCAFFOLDING
═══════════════════════════════════════════════════════════════════════════

Create these files. If a file already exists, READ it first and ASK before
overwriting (never silently clobber).

  ./CLAUDE.md
  ./.claude/CLAUDE.md
  ./.claude/commands/{push,review,test-quick,interview,handoff,codexreview,councilreview,lessons-audit}.md
  ./.claude/skills/                  (empty dir — skills go here as you build them)
  ./.claude/settings.json
  ./docs/architecture.md
  ./tasks/lessons.md
  ./README.md                        (only if missing)

──────────────────────────────────────────────────────────────────────────
2.1 — ./CLAUDE.md (root operating contract)
──────────────────────────────────────────────────────────────────────────

Sections in order:

  # {PROJECT_NAME} — Claude Operating Contract

  ## 0) Role
  - Primary execution agent. Implements, tests, reports.
  - DOES NOT: push without /push, spend money without confirmation,
    store/leak secrets, invent requirements.

  ## 1) Interview-First (mandatory for new tasks)
  - 10 questions before any non-trivial work. Use `/interview`.
  - "just do it" → confirm 3 critical assumptions first.

  ## 2) Plan-Then-Code
  - For >1-file or production-touching changes: enter plan mode.
  - Subagents: sonnet=research, haiku=lookups, opus=main only.
  - Parallel agents → use git worktrees to prevent conflicts.

  ## 3) Lessons-Driven Development
  - Before plan: read `tasks/lessons.md`, list relevant rules in plan
    as "Relevant lessons: #N, #M".
  - Severity legend:
      🔴 — data/money loss or security
      🟡 — bugs/UX
      ⚪ — style
    File `tasks/lessons.md` must start with this legend.
  - When fixing a 🔴 or 🟡 problem: add a rule to tasks/lessons.md.
  - Rule format: ONE-TWO sentences (forbidden/required + alternative +
    what breaks). Split if it covers more than one concern.
  - Each rule contains: severity, number, title, body. No commit hashes,
    no "Verify:" / grep instructions. Pattern names allowed when they
    ARE the rule, not metadata.
  - Reference existing functions/utilities by NAME — do not re-describe.
  - Group rules into sections by TECHNOLOGY AREA (Next, PostgreSQL,
    Solana, etc.) — never "Security", "General", "Cross-technology".
    Cross-cutting rules go to the technology where the fix lives.
  - `## Project rules` zone — anything project-local. NEVER autonomously
    modify rules in `## Project rules`; require explicit user confirmation.
  - If a new rule contradicts an existing one: investigate with user,
    do not auto-resolve.
  - After user correction:
    · Code/architecture mistake (🔴/🟡) → add rule to tasks/lessons.md
    · Behavior/workflow preference → ask "save to memory?", save only
      to memory if yes, never to lessons.md

  ## 4) Dual-Session Review
  - After every significant change (security, payments, new phases),
    run `/review`, then `/codexreview` for adversarial pass, then
    `/councilreview` for multi-expert pass.

  ## 5) Self-Improving Flywheel
  - Mistake → fix → rule (lessons.md or hook) → never repeat.

  ## 6) Language Rules
  - English: code, commits, README, PRs, docs.
  - Russian: chat with operator.

  ## 7) Security Rules (absolute)
  - Never commit / log: private keys (0x + 64 hex), `ak_live_*`,
    `ghp_*`, `.env*`, OAuth tokens, cookies.
  - Pre-commit / pre-push hooks block secrets in `src/`.
  - Token flow on push: set env var → push → unset.
  - Author: `Claude <noreply@anthropic.com>`.
  - Forbidden without explicit user instruction: `rm -rf` on data,
    `git push --force` to main, `git reset --hard`, `--no-verify`.

  ## 8) Execution Workflow (TDD-informed)
   1. Read first — relevant skill + lessons.md
   2. Interview — `/interview` if scope unclear
   3. Plan — enter plan mode, list "Relevant lessons: #..."
   4. Test first — write or identify the test that proves done
   5. Implement — minimal scope, no drive-by refactors
   6. Review — `/review` → `/codexreview` → `/councilreview`
   7. Verify — typecheck + tests + build (project-specific gate)
   8. Report — show diff stats; ask before /push

  ## 9) Custom Commands
  | Command | Purpose |
  |---|---|
  | /push           | Secret scan → commit → push → unset token |
  | /review         | Adversarial security review of recent diff |
  | /codexreview    | 8-category adversarial code audit |
  | /councilreview  | 5-expert council review |
  | /test-quick     | Project-defined fast test suite |
  | /interview      | 10-question intake |
  | /handoff        | Context bootstrap for new session |
  | /lessons-audit  | Generate stack rules + audit git history |

  ## 10) Communication Style
  - Concise. Lead with the answer.
  - Tables for comparisons. Bullets for lists.
  - Every error: WHAT happened, WHY, HOW to fix.
  - Distinguish server bug vs test bug vs SDK limitation.

  ## 11) Failure Policy
  - Unclear → ask
  - Real money → confirm first
  - Destructive git → confirm first
  - Ambiguous result → explain both interpretations
  - Possible secret leak → STOP immediately

──────────────────────────────────────────────────────────────────────────
2.2 — ./.claude/CLAUDE.md (project-specific)
──────────────────────────────────────────────────────────────────────────

Sections:

  # {PROJECT_NAME} — Project-Specific Rules

  Extends ../CLAUDE.md with project-specific state. Detailed domain
  invariants live in `.claude/skills/<area>/SKILL.md` files.

  ## Meta-Rules
  (10 rules — adapted to this project from the Phase-0 interview)

  ## Stack
  - Runtime / language versions
  - Package manager
  - Frameworks
  - DB / queue / cache
  - Deploy target

  ## Verification Gate
  - Exact command(s) to run before considering work done
  - Example: `pnpm typecheck && pnpm test && pnpm build`

  ## Invariants by Domain
  | Touching | Read skill | Covers |
  |---|---|---|
  | (filled as skills are created in `.claude/skills/`) | | |

  ## Known Bugs — DO NOT Reintroduce
  (initially empty — populated by `/lessons-audit` and ongoing fixes)

  ## Environment / Secrets
  - `.env.example` — committed
  - `.env` / `.env.local` — gitignored, never logged
  - Where each secret comes from (1Password / env / vault)

  ## Deployment Notes
  - Build steps
  - Health checks
  - Rollback procedure

──────────────────────────────────────────────────────────────────────────
2.3 — ./.claude/commands/*.md
──────────────────────────────────────────────────────────────────────────

Create eight files. Each is a self-contained markdown prompt — the body
becomes what Claude runs when the operator types the slash command.

──── push.md ────
Title: Safe Push to GitHub
Body:
  Pre-push checklist for THIS project.
   1. Syntax check changed files (project-specific — adapt to stack)
   2. Security scan: grep `src/` and root for
        - `0x[a-fA-F0-9]{64}`         (private keys)
        - `ghp_[A-Za-z0-9]{36,}`      (GitHub tokens)
        - `ak_live_[A-Za-z0-9]{20,}`  (live API keys)
        - `sk_live_[A-Za-z0-9]{20,}`  (Stripe live)
        - `eyJ[A-Za-z0-9_\\-]{20,}\\.eyJ` (JWTs)
      If any match → STOP, do not commit.
   3. `git diff --stat` and show summary to operator. Ask "commit?".
   4. On approval: `git commit -m "<msg>" --author "Claude <noreply@anthropic.com>"`
   5. Push using token from env: `GH_TOKEN=$(cat ~/.gh-tokens/{PROJECT_NAME})` →
      `git push` with token in remote URL → immediately reset remote URL to
      tokenless form. Never echo the token.
   6. Report URL of the pushed commit. Run `git status` to confirm clean.

──── review.md ────
Title: Adversarial Security Review (lightweight)
Body:
  Run `git diff HEAD~1` (or `git diff main...HEAD` on a branch).
  Check ONLY for:
    - hardcoded secrets
    - `console.log` / `print` of sensitive field names (password, token,
      privateKey, sk_, ak_, ssn, cardNumber)
    - `eval()`, `Function(...)`, `child_process.exec` with user input
    - sensitive data unredacted in error messages or stack traces
    - SQL string-concatenation instead of parameterized queries
  Output: severity-tagged findings. CRITICAL = block.

──── codexreview.md ────
Title: Adversarial Code Audit (8 categories)
Body:
  Analyse `git diff HEAD~1` (or `git diff main...HEAD` on a branch).
  For each changed file, check 8 categories:
    1. SECURITY        — secrets, injection, XSS, SSRF, auth bypass,
                         insecure crypto, eval(), exec()
    2. DATA INTEGRITY  — races, lost updates, unchecked nulls, silent fails
    3. ERROR HANDLING  — swallowed errors, catch-all without rethrow,
                         missing error boundaries
    4. BUSINESS LOGIC  — off-by-one, wrong comparison ops, inverted
                         conditions, edge cases
    5. PERFORMANCE     — N+1, unbounded loops, missing pagination, memory
                         leaks, missing indexes
    6. API CONTRACT    — breaking changes, missing validation,
                         inconsistent response shape, wrong status codes
    7. DEPENDENCIES    — unnecessary deps, known CVEs, version pinning,
                         unused imports
    8. OBSERVABILITY   — sensitive data in logs, missing audit trail,
                         no error context

  Output per finding:
    [SEVERITY] Category — Title
      File:   path:line
      Issue:  description
      Impact: what breaks if unfixed
      Fix:    concrete diff or code

  Severity:
    CRITICAL — blocker, do not push
    HIGH     — fix before merge
    MEDIUM   — tech debt
    LOW      — style/nit

  End with a decision: BLOCK / APPROVE WITH FIXES / APPROVE.
  Mode is adversarial — false positives preferred over missed flaws.
  Do NOT compliment the code. Only problems.

──── councilreview.md ────
Title: Multi-Expert Council Review
Body:
  Analyse `git diff HEAD~1` (or `git diff main...HEAD`).
  Run the changes through 5 expert roles. Each is INDEPENDENT and can
  veto. One BLOCK = council BLOCK.

    Security Architect    — attack surface, auth, crypto, injection,
                            secrets, OWASP Top 10
    Performance Engineer  — latency, throughput, memory, scaling
                            bottlenecks, caching
    Reliability Engineer  — failure modes, recovery, graceful degradation,
                            timeout handling
    API Designer          — contract stability, backward compatibility,
                            docs, DX
    Domain Expert         — adapt to DOMAIN parameter from setup.
                            For {DOMAIN}: business logic correctness,
                            edge cases, regulatory compliance

  Each expert gives:
    - 1-3 findings with severity
    - Decision: PASS / CONCERN / BLOCK

  Output footer:
    Council Decision: APPROVE / APPROVE WITH CONDITIONS /
                      REQUEST CHANGES / BLOCK
    Votes: Security=…, Performance=…, Reliability=…, API=…, Domain=…
    Critical items: …

──── test-quick.md ────
Title: Quick Project Test
Body:
  Run the project-defined fast test suite (single-line gate from
  .claude/CLAUDE.md "Verification Gate" section). Report PASS / FAIL
  per stage. On FAIL, classify root cause: code / test / infra / flake.

──── interview.md ────
Title: 10-Question Project Intake
Body:
  Ask the 10 questions from Phase 0 above. Loop until 0 ambiguous items.
  After: write summary to `tasks/intake-<YYYY-MM-DD>.md` and reference
  it from `.claude/CLAUDE.md`.

──── handoff.md ────
Title: Project Handoff — Context Bootstrap
Body:
  When starting a NEW session on this project, read these files in order:

   1. Project Rules — `./CLAUDE.md`, then `./.claude/CLAUDE.md`
   2. Lessons       — `./tasks/lessons.md` (legend + all rules)
   3. Memory        — find `~/.claude/projects/*/memory/MEMORY.md` matching
                      cwd, read index + all referenced files
   4. Skills        — list `.claude/skills/*/SKILL.md`, read each
   5. Architecture  — `./docs/architecture.md`
   6. Recent work   — `git log --oneline -10`
   7. Current state — `git status`, `git diff --stat`

  Report (≤ 12 lines):
    1. Project name + one-sentence description
    2. Stack summary
    3. Key facts (wallet / API keys location / server)
    4. Last 3 commits
    5. Any uncommitted changes
    6. Available commands
    7. "Ready to work. What do you need?"

──── lessons-audit.md ────
Title: Lessons Audit — generate stack rules + audit git history
Body:
  Two-phase audit of `tasks/lessons.md`.

  Phase A — Stack-Specific Rules (generative):
    1. Detect project stack (frameworks, DB, deploy target, versions).
    2. Generate rules for likely pitfalls in this stack combination —
       cover interactions between technologies, version-specific
       breaking changes, common traps per framework.
    3. Priority — rules that prevent data loss, security holes,
       silent failures.
    4. Cover all 🔴 / 🟡 risks for the stack; do not pad with low-value
       rules.
    5. Format strictly per `## 3) Lessons-Driven Development` in
       /CLAUDE.md.
    6. Group by technology section.
    ⏸️  STOP — show generated rules, await approval.

  Phase B — Git History Audit (if .git exists):
    1. `git log --all --oneline` — find all bug-fix commits
       (heuristic: "fix", "bug", "hotfix", "patch", "regression",
       "rollback", revert, "broken").
    2. For each: `git show <hash>` — extract WHAT broke, severity by
       consequence (🔴/🟡/⚪), root cause.
    3. For each 🔴/🟡 finding, check coverage in current lessons.md.
       Build table: covered / partial / not covered.
    4. Formulate missing rules.
    ⏸️  STOP — show audit report, await approval.

  Then:
    - Phase A rules → tasks/lessons.md in technology sections
    - Phase B rules → tasks/lessons.md in technology sections
    - Existing rules: do NOT touch (especially `## Project rules` zone).
    - Conflict with existing rule → ASK, do not auto-resolve.

──────────────────────────────────────────────────────────────────────────
2.4 — ./.claude/settings.json (hooks)
──────────────────────────────────────────────────────────────────────────

Create a project-local settings.json with two PreToolUse hooks. Each hook
runs the script below — if any match found in `src/`, exit 1 and abort
the tool call.

  {
    "hooks": {
      "PreToolUse": [
        {
          "matcher": "Bash",
          "filter": "git commit",
          "command": "bash .claude/hooks/secret-scan.sh"
        },
        {
          "matcher": "Bash",
          "filter": "git push",
          "command": "bash .claude/hooks/secret-scan.sh"
        }
      ]
    }
  }

Also create `.claude/hooks/secret-scan.sh`:

  #!/usr/bin/env bash
  set -e
  PATTERNS=(
    '0x[a-fA-F0-9]{64}'
    'ghp_[A-Za-z0-9]{36,}'
    'ak_live_[A-Za-z0-9]{20,}'
    'sk_live_[A-Za-z0-9]{20,}'
    'eyJ[A-Za-z0-9_-]{20,}\.eyJ'
    '-----BEGIN [A-Z ]*PRIVATE KEY-----'
  )
  for p in "${PATTERNS[@]}"; do
    if git diff --cached --diff-filter=AM | grep -EnH "$p" > /dev/null 2>&1; then
      echo "BLOCKED: secret-like pattern '$p' detected in staged diff."
      echo "If this is a false positive, set ALLOW_SECRET=1 and re-run."
      [ "${ALLOW_SECRET:-0}" = "1" ] || exit 1
    fi
  done

`chmod +x .claude/hooks/secret-scan.sh`.

──────────────────────────────────────────────────────────────────────────
2.5 — ./docs/architecture.md
──────────────────────────────────────────────────────────────────────────

Mermaid diagrams (placeholders Claude fills based on Phase 1 detection):
  - Component map        (boxes for app / db / cache / queue / external)
  - Main flow / pipeline (sequence or flowchart for the primary feature)
  - Deploy topology      (if multi-tier)
  - Data lifecycle       (only if the project handles user data)

──────────────────────────────────────────────────────────────────────────
2.6 — ./tasks/lessons.md (initial skeleton)
──────────────────────────────────────────────────────────────────────────

  # Lessons — {PROJECT_NAME}

  Severity legend:
  🔴 — data/money loss or security
  🟡 — bugs/UX
  ⚪ — style

  Add a rule when fixing a 🔴 or 🟡 problem. Format: ONE-TWO sentences
  (forbidden/required + alternative + what breaks). Group by technology
  section. Reference existing functions/utilities by name. Never edit
  `## Project rules` without explicit user approval.

  ## (technology sections appear here after `/lessons-audit`)

  ## Project rules
  (operator-managed — do not autonomously modify)

⏸️  STOP — after Phase 2 show created file tree, await approval to continue.

═══════════════════════════════════════════════════════════════════════════
PHASE 3 — STACK-SPECIFIC LESSONS (calls /lessons-audit Phase A)
═══════════════════════════════════════════════════════════════════════════

Run `/lessons-audit` Phase A (stack rules only — do NOT run Phase B yet).
Generate stack-specific rules for the detected technology combination.
Cover:
  - Interactions between technologies (Next + Vercel + KV, FastAPI + asyncpg, etc.)
  - Version-specific breaking changes
  - Common traps per framework
  - Priority on 🔴 / 🟡 risks (data loss, security, silent failure)

⏸️  STOP — present rules, await "yes write".
On approval: write to tasks/lessons.md.

═══════════════════════════════════════════════════════════════════════════
PHASE 4 — GIT HISTORY AUDIT (skip if no .git history)
═══════════════════════════════════════════════════════════════════════════

If `git log` returns commits: run `/lessons-audit` Phase B.
If empty repo or fresh init: skip with one-line note "no history to audit".

⏸️  STOP — present audit report, await "yes write".
On approval: append missing rules to tasks/lessons.md.

═══════════════════════════════════════════════════════════════════════════
PHASE 5 — ARCHITECTURE DIAGRAM
═══════════════════════════════════════════════════════════════════════════

Fill `docs/architecture.md` placeholders with concrete Mermaid based on
Phase 1 detection + Phase 0 answers. Don't invent components that don't
exist yet — only diagram what is actually wired or planned in interview.

⏸️  STOP — show rendered diagrams summary, await approval.

═══════════════════════════════════════════════════════════════════════════
PHASE 6 — MEMORY ENTRY
═══════════════════════════════════════════════════════════════════════════

Create memory entry that survives across sessions.

  Find the memory directory matching this cwd:
    ls ~/.claude/projects/ | grep "$(pwd | sed 's|/|-|g')"

  In that directory's memory/ subdir:
    - Append/update MEMORY.md with a single-line entry:
        - [project_{name}.md](project_{name}.md) — one-sentence hook
    - Create project_{name}.md with frontmatter:
        ---
        name: project-{name}
        description: <one-line>
        metadata: { type: project }
        ---
        Stack: ...
        Deploy: ...
        Key facts: (paths, ports, env locations)
        Why: <motivation from Phase 0>
        How to apply: <when to use this memory>

═══════════════════════════════════════════════════════════════════════════
PHASE 7 — README (only if missing)
═══════════════════════════════════════════════════════════════════════════

Skeleton:
  # {PROJECT_NAME}
  <one-sentence purpose>

  ## Quick start
  <commands from Phase 1 stack detection>

  ## Layout
  - `src/` …
  - `.claude/` — Claude Code operating contract + skills
  - `tasks/lessons.md` — accumulated do-not-repeat rules
  - `docs/architecture.md` — Mermaid diagrams

═══════════════════════════════════════════════════════════════════════════
PHASE 8 — VERIFY
═══════════════════════════════════════════════════════════════════════════

  1. Trigger `/handoff` to confirm context bootstrap reads everything
     created above. Report any path it could not find.
  2. Try `/test-quick` if the project actually has tests yet
     (skip with note otherwise).
  3. Try secret-scan hook with a fake matching string in a temp file —
     confirm it blocks. Remove temp file.
  4. Print final tree of created files with sizes.

═══════════════════════════════════════════════════════════════════════════
PHASE 9 — REPORT
═══════════════════════════════════════════════════════════════════════════

Final report (table form, ≤ 25 lines):

  | What            | Path                                | Status |
  |-----------------|-------------------------------------|--------|
  | Root contract   | ./CLAUDE.md                         | ✅     |
  | Project rules   | ./.claude/CLAUDE.md                 | ✅     |
  | Commands (8)    | ./.claude/commands/                 | ✅     |
  | Skills dir      | ./.claude/skills/                   | ✅     |
  | Hooks + script  | ./.claude/{settings.json,hooks/}    | ✅     |
  | Lessons         | ./tasks/lessons.md                  | ✅     |
  | Architecture    | ./docs/architecture.md              | ✅     |
  | README          | ./README.md                         | ✅     |
  | Memory          | ~/.claude/projects/…/memory/        | ✅     |

  Stack: <one-line>
  Verification gate: <one-line>
  Open questions: <if any from Phase 0>

  "Ready to work. What do you want to build first?"

═══════════════════════════════════════════════════════════════════════════
PRINCIPLES (apply across all phases)
═══════════════════════════════════════════════════════════════════════════

  1. Context engineering > prompt engineering — quality of CLAUDE.md,
     skills, hooks, lessons.md determines quality of work.
  2. Every mistake → a rule — flywheel: mistake → fix → rule (lessons.md
     or hook) → never repeat.
  3. Interview before code — eliminate ambiguity up front.
  4. Review before push — adversarial first, council second.
  5. Hooks are HARD rules — not advisory.
  6. TDD-informed — test first when possible; if not possible, say so.
  7. Parallel agents for research; worktrees for parallel writes.
  8. English in code, Russian in chat. Always.

═══════════════════════════════════════════════════════════════════════════
EXTERNAL REFERENCES
═══════════════════════════════════════════════════════════════════════════

When designing skills inside `.claude/skills/`, browse for prior art:
  - https://github.com/addyosmani/agent-skills
  - https://github.com/mattpocock/skills
  - https://github.com/garrytan/gstack

Copy patterns, not contents — adapt to project domain.
```

## ===== END OF PROMPT =====

---

## What the operator gets after running this prompt

After Claude completes all 9 phases:

```
<project>/
├── CLAUDE.md                       ← root operating contract
├── README.md
├── .claude/
│   ├── CLAUDE.md                   ← project-specific rules
│   ├── settings.json               ← hooks config
│   ├── commands/                   ← 8 slash commands
│   │   ├── push.md
│   │   ├── review.md
│   │   ├── codexreview.md
│   │   ├── councilreview.md
│   │   ├── test-quick.md
│   │   ├── interview.md
│   │   ├── handoff.md
│   │   └── lessons-audit.md
│   ├── hooks/
│   │   └── secret-scan.sh          ← blocks secrets on commit/push
│   └── skills/                     ← (empty — fill as you build)
├── docs/
│   └── architecture.md             ← Mermaid diagrams
└── tasks/
    └── lessons.md                  ← severity legend + technology sections
```

Plus a memory entry in `~/.claude/projects/<cwd-mapped>/memory/` so the
next Claude Code session in this directory boots with full context via
`/handoff`.

---

## Tips

- **Skip Phase 4** by saying so up front if the repo has only a single "init" commit.
- **Skip Phase 7** if README already has content you want to keep.
- For projects where chat language is English (not Russian), tell Claude in Phase 0 — it will adjust the CLAUDE.md.
- For monorepos: run this prompt at the **root** once, then inside each package add a thin `<package>/.claude/CLAUDE.md` linking back to the root and listing package-only conventions.
- After first real bug-fix: run `/lessons-audit` again to capture the rule before memory fades.

---

## Maintenance

When this template needs updating (new command, new principle, new known pitfall pattern):
1. Edit this file (`docs/new-project-setup-prompt.md` in workspace root)
2. Bump a date at the top: "Last revised: YYYY-MM-DD"
3. The next new-project bootstrap uses the updated version automatically.

---

## Token-optimization stack (install into every project by default)

**Goal:** cut inbound+outbound token spend without breaking the working system or losing quality. Four tools were
researched (2026-07-22); **install 3, defer 1**. All local, anonymous, offline. Add a "Token-opt" step to Phase 2 of the
bootstrap so every new project (and every fleet user) gets it.

### The tools and their assessments
| Tool | Repo | What it really is | Assessment |
|---|---|---|---|
| **RTK** | `rtk-ai/rtk` | **NOT an API proxy** (marketing word). A LOCAL command-output compressor via a Claude Code **PreToolUse Bash hook** (`git status`→`rtk git status`→compressed stdout). Never sees the LLM key/traffic. 60–90% on noisy cmds (git/npm/test/logs), ~0 on short. **PreToolUse hooks DO fire in `claude --print`** (verified) so it helps headless orchestras too. | **INSTALL — safest, biggest win** |
| **Ponytail** | `DietrichGebert/ponytail` | Behavior plugin injecting YAGNI "laziest senior dev" (write less code). ~22% fewer tokens. | **INSTALL at `lite`; `off` for LAW-governed / security / payments / infra work** (it changes generation behavior) |
| **Graphify** | `Graphify-Labs/graphify` | Local tree-sitter **code knowledge graph**; the agent queries the graph instead of grep+re-reading files. Fully local/offline for code (no LLM/embeddings/vector store). Graph is **per-repo**. | **INSTALL — audit its PreToolUse hook + exclude media/build dirs; keep `graph.json/html` out of git** |
| **Headroom** | `headroomlabs-ai/headroom` | A context-compression **proxy** that sees full prompts+code+secrets **cleartext** + caches originals in a local **plaintext** cache; only ~15–20% coding savings; overrides `ANTHROPIC_BASE_URL`. | **DEFER — do NOT run on secret-bearing servers.** MCP-mode on a laptop only, as a separate decision |

### Install commands (per user / per machine)
```bash
# 0) KILL-SWITCH BACKUP first (always)
cp ~/.claude/settings.json ~/.claude/settings.json.pre-tokenstack 2>/dev/null || echo '{}' > ~/.claude/settings.json
[ -f ~/.claude/CLAUDE.md ] && cp ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.pre-tokenstack

# 1) RTK — install binary
brew install rtk                                                   # macOS
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh   # Linux
grep -q 'local/bin.*PATH' ~/.bashrc || echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
export RTK_TELEMETRY_DISABLED=1 && rtk telemetry disable            # anonymous/offline

# 1b) RTK — WIRE THE HOOK BY jq-APPEND (never let `rtk init -g` clobber an existing hook)
RTKBIN="$(command -v rtk)"
RTKHOOK=$(jq -n --arg c "$RTKBIN hook claude" '{matcher:"Bash",hooks:[{type:"command",command:$c,timeout:10}]}')
jq --argjson h "$RTKHOOK" '.env=(.env//{})|.env.RTK_TELEMETRY_DISABLED="1"|.hooks=(.hooks//{})|.hooks.PreToolUse=((.hooks.PreToolUse//[])+[$h])' \
  ~/.claude/settings.json > ~/.claude/settings.json.tmp
jq . ~/.claude/settings.json.tmp >/dev/null 2>&1 && mv ~/.claude/settings.json.tmp ~/.claude/settings.json   # ATOMIC + validated

# 2) Ponytail
claude plugin marketplace add DietrichGebert/ponytail && claude plugin install ponytail@ponytail
echo 'export PONYTAIL_DEFAULT_MODE=lite' >> ~/.bashrc     # lite; set =off on LAW-governed orchestra users

# 3) Graphify (audit its hook first)
uv tool install graphifyy && graphify install             # writes a PreToolUse hook + a CLAUDE.md directive — REVIEW both
graphify . --exclude out --exclude '*.mp4' --exclude '*.wav'   # per-repo build, exclude heavy media/build
```

### Immutable laws (learned the hard way)
- A Claude Code hook **cannot kill a `claude --print` pass**: exit 2 = block that ONE tool-call (degradation), any other
  nonzero/timeout/missing-binary = non-blocking warning. **The ONLY fatal vector is an invalid `settings.json`** (Claude
  Code then ignores ALL settings). ⇒ **edit settings.json only via atomic `jq … > tmp && mv tmp settings.json` + validate**;
  **never let an installer overwrite an existing hook — jq-append to CHAIN** (keep matchers disjoint: RTK=`Bash`,
  Graphify=`Read|Grep|Glob`; both run).
- **Never set `ANTHROPIC_BASE_URL` on a server** — it would route every pass through a proxy = a single point of failure +
  confuses limit/"not-logged-in" heuristics. This is why Headroom's proxy mode is banned on any orchestra fleet.
- On users whose **Python gates read a driver command's output** (pytest / `python -m pipeline.*` / ffmpeg logs), RTK's
  lossy compression could flip a gate result silently → set `[tee] mode="failures"` in `~/.config/rtk/config.toml` and add
  those to `exclude_commands`. Install on orchestra users **only in an idle window** (empty `pgrep -f 'model claude'`).
- Anonymous/offline flags: RTK `RTK_TELEMETRY_DISABLED=1`; Graphify offline-by-default for code (query-log off); Ponytail
  static (audit `hooks/` for `curl|wget`). Prove offline empirically with `unshare -rn <bin> …` (no network).

### Kill switch (instant rollback, no restart — the next pass is a fresh process)
```bash
cat > ~/bin/tokenstack-off.sh <<'K'
#!/bin/sh
cp ~/.claude/settings.json.pre-tokenstack ~/.claude/settings.json
[ -f ~/.claude/CLAUDE.md.pre-tokenstack ] && cp ~/.claude/CLAUDE.md.pre-tokenstack ~/.claude/CLAUDE.md
claude plugin uninstall ponytail 2>/dev/null || true
K
chmod +x ~/bin/tokenstack-off.sh
```

---

## Professional GitHub setup — the realestate / audiobook2 pattern (make every serious project work like these)

Two production projects have a battle-tested GitHub setup: **realestate** (`<operator>/<project-a>`)
and **audiobook2** (`<operator>/<project-b>`). Reuse this pattern for any project that will grow laws,
run autonomous agents, or handle money/canon. It is the "everything is enforced, nothing drifts, no self-report is trusted"
model. Add these to Phase 2 (scaffolding) + Phase 8 (verify) of the bootstrap.

### 1. Repo layout + author + push discipline
- Private GitHub repo; commits `Author: Claude <noreply@anthropic.com>`; **never `--no-verify`**, never `git push --force`
  to main, never `git reset --hard` without confirmation.
- Push flow = `/push`: secret-scan → commit → push with token from env → **unset the token immediately** (never echo it).
- Multi-agent writes are **flock-serialized** by `scripts/git_txn.sh` (a repo-lock so concurrent agents don't race a commit).
- Auto-merge is allowed only for a completed, self-reviewed "round" (super-review); everything else awaits operator `/push`.

### 2. CI = GitHub Actions, the same gate on every PR (spec lives in `TECHNOLOGY_STANDARDS §CI`)
Mirror realestate's `.github/workflows/`:
- **Ruff (lint)** → `ruff check <src> <tests>`
- **mypy (types)** — whole-tree, install ALL optional extras so mypy follows imports (a narrow local mypy misses errors)
- **pytest + coverage gate** → `pytest --cov --cov-report=term-missing --cov-fail-under=<N>` (realestate: 84)
- **Secret scanning** — gitleaks-action (scoped to the PR's commits) and/or TruffleHog; plus Snyk/CodeQL where useful
- **Consistency / domain suites** run as ordinary pytest tests (e.g. the booking-DB state-machine suite)
- Merge only when CI is green (realestate ships "5/5 jobs green"). A red **whole-tree** run beats a green filtered subset —
  always run the BARE full suite before declaring done (a filtered gate once let a red suite sign off).

### 3. The governance CIRCUIT — every "truth" edit is gated (audiobook2's `truth.lock`)
The strongest idea to copy. "Truth" files = laws, skills, expert/judge councils, prohibitions, canon, load-bearing configs.
- `truth.lock` pins a hash of every truth file. Editing one is a **HARD GATE**: the same commit must carry the 4 circuit
  artifacts — **analysis → change-impact → independent review (a Fable / adversarial pass) → test evidence** — plus a
  `TRUTH_CHANGES.md` (TC-NNN) entry, and re-hash `truth.lock`. A pre-commit hook enforces it; **never `--no-verify`**.
- A truth edit **outside a pre-registered change-set is a STOP** — the agent asks the operator, never self-authorizes
  (e.g. an author/expert council edit, or granting itself publish authorization).
- **Fixes-become-laws:** a fix isn't done until it's a `law + gate + test` so future work inherits it. A law with no wired
  gate is a defect.

### 4. Laws + enforcement anchors (no orphan rules)
- Laws live in `tasks/lessons.md` (numbered/named, grouped by technology — see §3 of the root CLAUDE.md), compacted
  periodically (merge/archive, never silently drop a behavioral rule).
- `enforced_by.yaml` anchors **every law to the code gate + test that enforces it**; a ratchet fails the build on any
  **dangling** law (rule with no wired enforcement) — so laws can't rot into comments.

### 5. ADRs — one per real decision
- `docs/adr/ADR-NNNN-*.md` (audiobook2 has 74) or `implementation/decisions/ADR-NNNN-*.md` (realestate). Each records the
  decision + why + what it reverses. Written **in the same PR as the code**, not after.

### 6. Docs can't drift from code (the SSOT gate)
- `scripts/gen_arch_facts.py` → `docs/ARCH_FACTS.json` derives architecture facts **from code** (truth-file count, gate
  list, model map, counts). A doc-consistency test fails when `ARCHITECTURE.md` / `PROJECT_STATUS.md` diverge from the
  derived facts — so the docs are provably current, not aspirational.

### 7. Secret hooks (defence in depth on top of CI)
- Local pre-commit / pre-push hook greps the staged diff for `0x[0-9a-f]{64}`, `ghp_…`, `ak_live_…`, `sk_live_…`, JWTs,
  `BEGIN … PRIVATE KEY` and **blocks** (see the `secret-scan.sh` in Phase 2.4). Secrets live only in `~/.env` /
  `~/.claude/*.env` — never committed, echoed, or logged.

### 8. Autonomous-round model (how work is executed on these repos)
- Work ships as numbered **rounds/phases** (realestate `R##`, audiobook2 `SI`/`W#`/`P#`). **Each step = law + gate + test +
  ADR, merged together.** An Opus supervisor loop executes; **Fable** (analysis-only model) writes the plan + adversarially
  reviews before code; the operator gates money, public publishing, and canon.
- **Verify against the SHIPPING path, never a self-report** — the operator's #1 law. Every "done" is re-checked against the
  code that actually runs (a green test on a paraphrase, a "kill" measured on a proxy, a "429 that never happened" — all
  real misses this pattern caught). A QA loop (page → structurer → class-router → circuit) turns human/browser review into
  landed laws so the system self-improves.
