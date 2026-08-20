# What this is, and what it is not

## Following these documents has no effect on any verdict

Provek verification measures **observed operations**. It does not check for the use of any method,
including this one. There is no field in the scorer for "used our method", and there could not be:
the score is deterministic code over measured quantities, and a method is not a measured quantity.

That is not a promise of restraint. It is a property of the instrument, and it is checkable — the
scorer and every gate are public at
[github.com/whiteknightonhorse/provek](https://github.com/whiteknightonhorse/provek).

## This is provenance, not teaching

These are the operating documents that produced provek.dev and the arrangement in which it was
built. They are published for one reason: a verifier that publishes its methodology should publish
how it was itself made, because a verdict nobody can reproduce is worth nothing, and neither is a
method whose author will not show their own work.

They are records of what was done. They are not a course, and there is no course. If one ever
exists it will be a different product with its own published decision, because a verifier selling
instruction in passing its own examination would be grading work it set.

## The separation, and why it is a whole repository

The project specification anticipated this conflict before any of it was written:

> If the same party teaches people to pass its own verification, it is grading work it set itself.
> Accepted for the MVP: verification is free, so the payment conflict does not arise; **teaching and
> verification are separated as components.**

"Separated as components" is a boundary a third party can check. So this corpus lives in its own
repository — not a section of the verification site, not a subdomain of convenience. The
verification surface contains no teaching, this repository contains no verdicts, and a single
sentence on the Method page is the only link between them.

The boundary is enforced by machines rather than intentions, in both directions:

- **Here:** a CI check fails the build if this repository mentions the verification instrument —
  its ladder levels, its passports, its evidence classes. The check is run against a deliberately
  planted violation and the failing run is kept in [`evidence/`](evidence/), because a gate never
  seen to fail is not evidence that anything is being caught.
- **There:** a test over the emitted site asserts this corpus is referenced exactly once, on the
  Method page, framed as provenance.

It is built this way now rather than later on purpose. Verification is free today; when it is paid,
the conflict returns with money attached, and the separation will already be structural instead of
being negotiated under pressure.

## Licence

[CC BY 4.0](LICENSE). Attribution to Provek, and a link back, is all that is asked.
