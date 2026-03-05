# Self-Evolution Protocol

## Evolution Triggers

### BEFORE Coding (Apply Knowledge)
- At **session start**: Read Anti-Patterns + Learned Skills sections below
- Before **any significant task**: Cross-check relevant skills — use best patterns, avoid known pitfalls
- When working on **new projects**: Check if any learned skill transfers

### AFTER Coding (Capture Knowledge)
- After completing a significant task (multi-file changes, new feature, bug fix)
- After making a mistake or needing to redo work
- After discovering a better approach mid-task
- After working on a new project for the first time
- When {USER_NAME} corrects {AGENT_NAME} or changes the approach

## Evolution Actions
What {AGENT_NAME} can do:
- **Add Rule**: New pattern discovered → add to identity/CLAUDE.md
- **Update Rule**: Existing rule is outdated or incomplete → refine it
- **Add Anti-Pattern**: Mistake made → log it so it never repeats
- **Add Skill**: New technique learned → track it
- **Transfer Pattern**: Pattern works in Project A → check if it applies to Project B

## Self-Reflection Template
After significant work, {AGENT_NAME} asks itself:
1. Did I discover a new pattern worth remembering?
2. Did I make a mistake I should prevent in the future?
3. Is there a rule I should update based on this experience?
4. Can anything I learned here help other projects?

## Evolution Log
Track all self-improvements with version history.

| Date | Type | What Changed | Trigger | Applied To |
|------|------|-------------|---------|------------|
<!-- Entries will be added automatically as {AGENT_NAME} evolves -->

## Learned Skills
Track techniques and patterns learned across all projects.

<!-- Example:
### Skill: Inertia File Upload
- **Learned from**: Project X
- **Pattern**: Use `router.post` with `forceFormData: true` + `_method: 'PUT'` for updates
- **Why**: `useForm.put()` ignores transformed payload
- **Applied to**: All Inertia projects
-->

## Anti-Patterns
Track mistakes to never repeat.

<!-- Example:
### Anti-Pattern: Setting status before payment confirms
- **What happened**: Set subscription to "active" on creation, before payment completed
- **Impact**: Orphaned active subscriptions when payment failed
- **Rule**: NEVER set paid/active status until payment callback confirms success
- **Applies to**: All payment integrations
-->
