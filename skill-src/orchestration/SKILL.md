---
name: orchestration
description: Team-lead orchestration for Claude Code on a Claude Pro plan, built for a 2-person hackathon. The main loop (Fable 5.2, Opus as fallback, never Sonnet) leads; sub-agents on Opus or Sonnet do the work. Three modes - mimari (architecture + working contract), insa (build), final (freeze + pitch). Load at project start, when the user says /orchestration [mimari|insa|final], and whenever spawning sub-agents or planning delegation.
---

# Orchestration (hackathon edition, Claude Pro)

Adapted from avenoxai/avenoxskills `fable-orchestration` (MIT).

Core law: **the lead's tokens buy judgment, not throughput.** The lead plans, splits, briefs, decides and verifies. Workers write code. The lead's context stays lean so it never hits compaction.

## Who leads

- **Lead = Fable 5.2** by default (`/model fable`).
- **Fallback lead = Opus 5.5** (`/model opus`) when Fable usage gets heavy: if Fable has used more than about half of its allowance and many hours remain, or the 5-hour window is nearly gone. Tell the user when you think it is time to switch.
- **Sonnet never leads.** Sonnet is a worker only.

## Mode

Pick the mode from the argument (`/orchestration mimari|insa|final`) or the user's words. If none is given: `ARCHITECTURE.md` missing or still the empty template (no Contract rows, no Tasks rows) → mimari; filled in and the user hasn't said freeze → insa. When in doubt, ask the user which mode. Say which mode you are in.

## Routing (all modes)

| Work | Goes to | Call | Brief |
| --- | --- | --- | --- |
| Architecture, contract, hard calls, splitting, verification decisions, synthesis | **Lead** | itself | n/a |
| Hard pieces: NASA data transforms, algorithms, real debugging, multi-file features, integration review | **Opus** | `model: "opus"` | Loose: goal, why, context it can't find, constraints, definition of done |
| Normal pieces: UI components, endpoints, scoped edits, recon, reading/summarizing, scripts | **Sonnet** | `model: "sonnet"` | Tight: files it may touch, ordered steps, output, what not to touch, when to stop and report |

Data cleanup is done by a worker writing a Python script, not by a model reading rows.

## Hard rules

1. **Every Agent call passes `model: "opus"` or `model: "sonnet"`.** Never omit it (omitting inherits the lead's model). Never spawn a Fable sub-agent.
2. **Max 2 sub-agents at once.** Both team members share nothing, but each account has one 5-hour pool that Fable and all its sub-agents drain.
3. **Pick the tier by difficulty.** Clearly hard → Opus directly. Clearly routine → Sonnet. Only when truly unsure: Sonnet first, escalate once on failure.
4. **Lead keeps context lean.** No big file reads, no feature implementation. The lead MAY do glue code, config, one-line fixes and reading one small known file.
5. **Verify with machines first.** A worker finishing code must run the build / tests / the app and report the output. "Done" is only said after that output (or the lead's own check) shows it works.
6. **Independent review only at integration points** (real data wired in, frontend↔backend joined, before deploy): a fresh agent (Opus) with a "find what breaks" brief. The writer never reviews its own work.
7. **Stay in your lane.** This member's agents touch only their own area (`backend/` or `frontend/`) plus their own backlog file. `shared/` and `ARCHITECTURE.md` change only by agreement between the two humans; say so to the user when a change is needed.
8. **Parallel workers never share files.** Each brief lists the exact files that worker may touch.
9. **Scripts in Python, not bash.** One teammate is on plain Windows.

## Mode: mimari (first ~2 hours, Fable)

Goal: a design that matches the real data, and a working contract both people can build against.

1. **Real-data recon** (1-2 Sonnet agents): download a real sample of each NASA dataset / call each API we plan to use. Report: format, size, fields, quirks, rate limits, whether it works at all. Summaries straight back to the lead (no report files).
2. **Decide** the design from what the data really looks like.
3. **Write `ARCHITECTURE.md`** from the template: problem + demo story, components, data flow, the contract, task list with owners, rejected alternatives and why, anti-goals.
4. **Contract as code**: `shared/mock/*.json` with realistic sample responses (built from the real sample), plus a backend skeleton that serves exactly these mocks on the agreed endpoints. Frontend builds against it from minute one.
5. **Backlogs**: fill `BACKLOG_BACKEND.md` and `BACKLOG_FRONTEND.md` from the task list.
6. **Deploy plan**: name where backend and frontend go live; target a deployed hello-world by hour 6.

## Mode: insa (build)

1. Read `ARCHITECTURE.md` and your own backlog file. Pull first (`git pull`).
2. Take the next task, brief a worker per the routing table, ≤2 at once, disjoint files.
3. Worker runs build/test/app → you check the output → mark done in your backlog file.
4. Keep the mock contract working: when real data replaces a mock, response shape must stay the same, or agree a change with the teammate first.
5. Keep the **static fallback**: the frontend must be able to run from `shared/mock` (or a pre-baked real-data JSON) if the backend is down.
6. At integration points, send an independent Opus reviewer (rule 6).
7. Commit small and often; update your backlog file at the end of each work block so any new session can resume from it.

## Mode: final (last ~4 hours)

1. **Code freeze.** Only fix what breaks the demo. No refactors, no "cleaner" rewrites, no new features.
2. **Jury simulation**: look up the official NASA Space Apps judging criteria (spaceappschallenge.org), then act as the jury: score the project against each criterion, list the questions they will ask and the weak spots (scientific validity, use of NASA data, impact).
3. **Pitch**: write the demo script and talk track for the required format and time limit (check the event rules).
4. **Polish**: small, safe UI touches only (copy, spacing, loading states, a clear first screen).
5. **Backup**: make sure the static-fallback demo works offline; have a screen recording of the demo.

## Files

- `CLAUDE.md` – project rules (points here)
- `ARCHITECTURE.md` – design + contract + task list + rejected alternatives
- `BACKLOG_BACKEND.md`, `BACKLOG_FRONTEND.md` – one per person, never edited by the other side's agents
- `shared/mock/` – contract sample responses
- Templates for these are in `templates/`

The user can override any rule for the session.
