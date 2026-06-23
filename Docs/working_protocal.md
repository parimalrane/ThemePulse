# TABELA — WORKING PROTOCOL

## PHASE 1 — AUDIT FIRST

Before changing anything:

Review current architecture.

Challenge assumptions.

Ask:

Is this module already good enough?

Can bad scoring contaminate output?

Are we solving correct problem?

No coding allowed in this phase.

---

## PHASE 2 — DESIGN REVIEW

Before writing code:

Design logic from all required perspectives:

• Senior Architect
• Quant Researcher
• Institutional Trader
• Market Maker
• Professional Momentum Trader

Question every assumption.

Challenge architecture aggressively.

No coding allowed in this phase.

---

## PHASE 3 — IMPLEMENTATION PLAN

Before code changes:

Identify exact files to modify.

Example:

Modify:

• main.py
• scoring_engine.py
• config.py

Create:

• new_engine.py

Delete:

• experimental_engine.py

No code generation before file impact review.

---

## PHASE 4 — SAFE IMPLEMENTATION

Code changes must be minimal.

Rules:

Never modify multiple files unnecessarily.

Protect stable modules.

Preserve backward compatibility.

Prefer replacing only required files.

Avoid architecture drift.

---

## PHASE 5 — OUTPUT VALIDATION

After running TABELA:

Review actual terminal output.

Ask:

Would professional traders care?

Would institutional traders care?

Would I personally open these charts?

If output quality is poor:

Reject implementation.

Rollback immediately.

Code correctness is irrelevant if output quality is poor.
