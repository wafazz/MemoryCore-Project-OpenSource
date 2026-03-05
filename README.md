# MemoryCore Project OpenSource

**A persistent memory system for Claude Code (or any AI coding agent).**

Turn your AI coding assistant into a self-improving engineering partner that remembers everything across sessions — patterns, mistakes, project context, and learned skills.

---

## What Is This?

MemoryCore is a structured memory architecture that gives your AI agent:

- **Persistent memory** — remembers your projects, patterns, and preferences across sessions
- **Self-evolution** — learns from mistakes and gets better over time
- **Pattern library** — reusable solutions indexed by problem type, built from YOUR projects
- **Protocols** — structured approaches for debugging, deployment, code review, project setup, and more
- **Session continuity** — pick up exactly where you left off

Built by [Fakrul](https://github.com/wafazz) after 130+ hours of coding with Claude Code across 17 projects.

---

## Architecture

```
~/.claude/CLAUDE.md ◄── Entry point (loaded every session)
     │
     ▼
~/MemoryCore/
├── 00-identity.md ·················· Agent identity & preferences
├── 05-workflow-guide.md ············ Session budget & token tips
├── 06-session-memory-format.md ····· Hot memory template
├── 07-self-evolution.md ············ Skills, anti-patterns, evolution log
├── 08-mimic-protocol.md ··········· Stack migration protocol
├── core-pattern-library.md ········· Reusable solutions by problem type
├── core-review-protocol.md ········· Code review checklist
├── core-init-protocol.md ··········· New project scaffolding
├── core-deployment.md ·············· Deploy recipes & checklists
├── core-learn-protocol.md ·········· Auto-learn new tech stacks
├── core-debug-protocol.md ·········· Structured debugging
├── core-git-workflow.md ············ Branch, commit, PR conventions
├── core-handoff-protocol.md ········ Client delivery protocol
└── Projects/
    └── _template.md ················ Per-project memory template
```

### Three Memory Layers

| Layer | Scope | Resets? |
|---|---|---|
| **Permanent** | Identity, protocols, pattern library, evolution log | Never |
| **Project** | Per-project profile, stack, patterns, decisions | Never (per project) |
| **Session** | Current tasks, working memory, recent changes | At 500 lines (recap survives) |

---

## Features

### 10 Commands

| Command | What It Does |
|---|---|
| `{agent} init` | Start new project with experience baked in |
| `{agent} learn` | Activate Learn Mode for unfamiliar tech stack |
| `{agent} deploy` | Deployment recipe + post-deploy checklist |
| `{agent} debug` | Structured debugging (classify → isolate → fix) |
| `{agent} handoff` | Prepare project for client delivery |
| `{agent}-Evolve` | Force self-reflection and knowledge capture |
| `mimic this` | Migrate project to a different tech stack |
| `show stats` | Token usage & session analytics |
| `show guide` | Workflow tips for Claude Pro users |

### 10 Protocols

| Protocol | Purpose |
|---|---|
| **Self-Evolution** | Learn from every session — track skills, anti-patterns, improvements |
| **MIMIC** | Migrate projects between tech stacks ("same heart, different armor") |
| **Init** | Bootstrap new projects with accumulated experience |
| **Learn** | Auto-learn new tech stacks on first use, graduate after first project |
| **Review** | 10-category code review checklist before delivering |
| **Debug** | Three Strikes Rule — structured diagnosis, don't go in circles |
| **Git Workflow** | Branch naming, commit conventions, PR templates |
| **Deployment** | 4 deploy recipes + env vars + troubleshooting |
| **Handoff** | 6-phase client delivery (docs → cleanup → deploy → archive) |
| **Session Memory** | Hot memory with auto-reset at 500 lines |

---

## Installation

### Quick Setup (Recommended)

```bash
# 1. Clone the repo
git clone https://github.com/{your-username}/MemoryCore.git

# 2. Run the setup script
cd MemoryCore
chmod +x setup.sh
./setup.sh
```

The setup script will ask you:
1. **Agent name** — what to call your AI agent (e.g. "Atlas", "Nova", "Iris")
2. **Your name** — so the agent knows who it's working for
3. **MemoryCore location** — where to store the memory files

It then:
- Copies all memory files to your chosen location
- Installs `CLAUDE.md` to `~/.claude/`
- Sets up the stats script
- Replaces all placeholders with your names

### Manual Setup

If you prefer to set up manually:

1. Copy the `memory/` folder to your preferred location (e.g. `~/MemoryCore/`)
2. Copy `.claude/CLAUDE.md` to `~/.claude/CLAUDE.md`
3. Copy `.claude/agent-stats.py` to `~/.claude/agent-stats.py`
4. Edit `~/.claude/CLAUDE.md` — replace `{AGENT_NAME}` with your agent's name
5. Edit `~/.claude/CLAUDE.md` — replace `{USER_NAME}` with your name
6. Edit `~/.claude/CLAUDE.md` — replace `{MEMORY_PATH}` with your MemoryCore folder path
7. Edit `memory/00-identity.md` — same replacements

---

## How It Works

### Session Start
```
You open Claude Code
  → CLAUDE.md loads automatically (identity, rules, commands)
  → Agent reads session-memory.md (if exists) for instant context
  → Agent reads self-evolution (anti-patterns to avoid, skills to apply)
  → Ready to code with full context
```

### During Coding
```
You work on features
  → Agent pulls patterns from Pattern Library
  → Agent runs Review Protocol after significant changes
  → Agent captures new patterns/gotchas in real-time
  → Session memory tracks current tasks and decisions
```

### Session End
```
You finish working
  → Agent updates session-memory.md (recap for next session)
  → Agent updates project profile in MemoryCore
  → Self-evolution captures new skills and anti-patterns
  → Next session starts exactly where you left off
```

### Over Time
```
Project 1: Agent learns your stack, patterns, preferences
Project 2: Agent applies learned patterns, avoids past mistakes
Project 3: Agent recommends stack, scaffolds with experience
Project N: Agent is a full engineering partner
```

---

## Customization

### Adding Your Own Patterns

After completing a project, add patterns to `core-pattern-library.md`:

```markdown
## My Stack Patterns

### Authentication with NextAuth
- **Stack**: Next.js + NextAuth
- **Problem**: Social login with role-based access
- **Solution**: NextAuth with custom adapter + middleware
- **Files**: auth.ts, middleware.ts
- **Gotchas**: Session callback must include role
- **First used in**: MyProject
```

### Adding Stack-Specific Review Checks

Add to `core-review-protocol.md`:

```markdown
### Next.js
- [ ] Server components don't use client hooks (useState, useEffect)
- [ ] API routes have proper error handling
- [ ] Middleware checks auth on protected routes
```

### Adding Deployment Recipes

Add to `core-deployment.md`:

```markdown
### Recipe X: Next.js on Vercel
1. Connect GitHub repo
2. Set environment variables
3. Deploy (automatic on push)
```

---

## Philosophy

MemoryCore is built on these principles:

1. **Start from experience, not from zero** — every new project benefits from past projects
2. **Learn once, apply forever** — mistakes become anti-patterns, solutions become patterns
3. **Three memory layers** — permanent knowledge, project context, session state
4. **Self-improving** — the agent gets better with every session
5. **Stack-agnostic** — works with any language, framework, or tool
6. **Your patterns, your way** — the structure is universal, the content is yours

---

## FAQ

**Q: Does this only work with Claude Code?**
A: It's designed for Claude Code but the concept works with any AI assistant that reads instruction files. Adapt `CLAUDE.md` to your tool's format.

**Q: Do I need all the protocols?**
A: No. Start with just `CLAUDE.md` + `00-identity.md` + `session-memory-format`. Add protocols as you need them.

**Q: Will my data be shared?**
A: No. Everything stays on your local machine. MemoryCore is just markdown files.

**Q: How much does this cost?**
A: Free. It's just markdown files and a Python script. You need a Claude Code subscription to use it.

**Q: Can I use a different agent name?**
A: Yes! The setup script lets you name your agent anything. "Atlas", "Nova", "Sage", "Bolt" — whatever you want.

---

## Credits

Built by **Fakrul** with **Iris** (Claude Opus 4.6).

- 130+ hours of real coding sessions
- 17 projects across PHP, Laravel, React, TypeScript, Filament, Livewire
- 122 sessions, 31K+ messages, 11K+ tool calls
- Every protocol battle-tested on real production projects

---

## License

MIT — use it, modify it, share it. If it helps you, star the repo.
