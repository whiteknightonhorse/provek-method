# How this instrument was built

The operating documents that produced [provek.dev](https://provek.dev) — a verification layer that
measures, from evidence, how much of a business runs without a human in the loop.

They are published for one reason. A verifier that asks the world to trust a published methodology
should be willing to publish how it was itself made. A verdict nobody can reproduce is worth
nothing; so is a method whose author will not show their own work.

**This is not a course, and there is no course.** Following these documents has no effect on any
verdict — the scorer is deterministic code over measured quantities, and "used our method" is not
one of them. Read [`DISCLAIMER.md`](DISCLAIMER.md) before anything else; it explains the separation
between teaching and verification, why it is an entire repository rather than a page, and how a
machine holds it rather than an intention.

## The documents

| | what it is | what it produced |
|---|---|---|
| [01 — design method](documents/01-design-method.md) | Six phases for building an interface that cannot be identified as machine-generated: interrogate first, clone a proven structure, then three parallel variants judged against a threshold. | Every screen on provek.dev, including the audit that caught its central visual mark sitting below the contrast floor it needed. |
| [02 — skill architecture](documents/02-skill-architecture.md) | Small independent skills instead of one framework. Requirements by interrogation, a specification with no code in it, tickets cut vertically, review in a fresh context. | The specification, the decision log, and the sixteen-ticket plan the verification pipeline was built from. |
| [03 — agent fleet](documents/03-agent-fleet.md) | A closed-loop arrangement of specialised agents with an independent approval agent as the governance layer, rather than a human approval step. | The arrangement this project runs inside — including the approval agent that ruled on the architecture of this very repository, and overruled its author twice while doing so. |
| [04 — project bootstrap](documents/04-project-bootstrap.md) | The skeleton a new project starts from: a registry of rules where each names the gate and test that enforce it, ratchets that fail the build, and a token-optimisation stack. | The repository layout, the law registry, and the gates that later caught four defects in the commit that fixed the previous four. |

Each document carries a provenance header: what it is, the sha256 of the original it was translated
or published from, and what was changed before publication. Documents 01 and 02 were translated from
Russian; 03 and 04 were already in English and are published as they stood, with account names
replaced and a handful of ordinary English words reworded so the separation gate can stay strict.

## What is honest about this, and what is not

**Honest:** these really are the documents. The design method really did produce the site, phase by
phase, including its failures — the site shipped a mark below its contrast floor, a scroll reveal
that would have left text permanently dimmed, and a soft 404 that answered "200 OK" for pages that
did not exist. All three were caught by following the method's own audit steps, and all three are
recorded in the verification repository's decision log.

**Not claimed:** that following them produces a good result. They were written for one operator and
one fleet, they assume specific tools, and they are opinionated in ways that suited this project and
may not suit yours. They are evidence of a method, not proof of one.

## The separation, in one paragraph

The project's specification anticipated the conflict before any of this existed: a party that
teaches people to pass its own verification is grading work it set itself. Its mitigation is that
teaching and verification stay separated as components. That is why this is its own repository, why
the verification site links here exactly once and in prose, and why a CI check fails this build if
this corpus so much as names the instrument — a check that is itself run against a deliberately
planted violation on every push, because a gate never seen to fail proves nothing. The failing run
is kept in [`evidence/`](evidence/).

## Licence

[CC BY 4.0](LICENSE). Attribution to Provek with a link back is all that is asked.
