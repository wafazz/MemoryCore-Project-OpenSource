# Learn Protocol
> "First time? Learn fast. Second time? Already mastered."

Activates automatically when {AGENT_NAME} detects a stack/technology not yet in the Pattern Library.

---

## Detection Trigger

{AGENT_NAME} checks during init or at session start:
1. Is this stack in the Pattern Library? → No → **Learn Mode ON**
2. Is this framework in the Init Protocol's recommendation table? → No → **Learn Mode ON**
3. Did {USER_NAME} explicitly mention an unfamiliar stack? → **Learn Mode ON**

Manual trigger: **"{AGENT_NAME} learn"**

---

## Phase 1: Research Sprint (Before Coding)

### 1a. Stack Profile
Gather and document:
- Official docs URL
- Package manager
- Scaffold command
- File structure convention
- Config files needed
- Dev/build/test commands

### 1b. Ecosystem Mapping
Map the new stack to concepts {AGENT_NAME} already knows:

| Concept | Known Equivalent | New Stack Equivalent |
|---|---|---|
| ORM | ? | ? |
| Auth | ? | ? |
| Routing | ? | ? |
| Middleware | ? | ? |
| Validation | ? | ? |
| Template/View | ? | ? |
| CLI | ? | ? |
| Queue | ? | ? |
| Cache | ? | ? |

### 1c. Gotcha Research
Search for common pitfalls:
- Known breaking changes
- Common beginner mistakes
- Performance footguns
- Security considerations
- Deployment quirks

---

## Phase 2: Build & Capture (During Coding)

While building, capture patterns in real-time:
1. **New pattern?** → Add to Pattern Library
2. **Gotcha found?** → Add to Anti-Patterns
3. **Equivalent found?** → Update ecosystem mapping
4. **Config trick?** → Document in project profile
5. **Package discovered?** → Log with version

### Capture format:
```markdown
### [Pattern Name]
- **Stack**: [e.g. Bun + Hono]
- **Problem**: [What you're solving]
- **Solution**: [Code pattern or approach]
- **Gotchas**: [What to watch out for]
- **First used in**: [Project name]
```

---

## Phase 3: Graduate (After First Project)

When the first project in the new stack is complete:

1. **Update Pattern Library** — add new stack section with all captured patterns
2. **Update Init Protocol** — add to recommendation table
3. **Update Review Protocol** — add stack-specific checklist
4. **Update Deployment Memory** — add deploy recipe
5. **Update Ecosystem Mapping** — save completed mapping
6. **Log Evolution** — entry in Self-Evolution log

---

## Phase 4: Cross-Pollinate

Check if patterns from the new stack can improve existing projects or vice versa.

---

## Learn Mode Indicator

When Learn Mode is active:
- Add `[LEARN]` tag to session-memory.md status
- Capture patterns more aggressively
- Document more thoroughly (building the knowledge base)

When graduated: remove `[LEARN]` tag, stack gets full support.
