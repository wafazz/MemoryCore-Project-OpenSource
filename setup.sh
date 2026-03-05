#!/bin/bash

# MemoryCore Setup Script
# Sets up your AI agent's persistent memory system

set -e

BOLD='\033[1m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo ""
echo -e "${BOLD}╔══════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║         MemoryCore Setup                 ║${NC}"
echo -e "${BOLD}║   Persistent Memory for AI Agents        ║${NC}"
echo -e "${BOLD}╚══════════════════════════════════════════╝${NC}"
echo ""

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Step 1: Agent name
echo -e "${CYAN}Step 1/3: What do you want to name your AI agent?${NC}"
echo "  Examples: Atlas, Nova, Sage, Iris, Bolt, Aria"
read -p "  Agent name: " AGENT_NAME

if [ -z "$AGENT_NAME" ]; then
    echo "Agent name cannot be empty. Exiting."
    exit 1
fi

# Step 2: User name
echo ""
echo -e "${CYAN}Step 2/3: What is your name?${NC}"
read -p "  Your name: " USER_NAME

if [ -z "$USER_NAME" ]; then
    echo "User name cannot be empty. Exiting."
    exit 1
fi

# Step 3: Memory location
DEFAULT_PATH="$HOME/MemoryCore"
echo ""
echo -e "${CYAN}Step 3/3: Where should MemoryCore be stored?${NC}"
echo "  Press Enter for default: $DEFAULT_PATH"
read -p "  Path: " MEMORY_PATH

if [ -z "$MEMORY_PATH" ]; then
    MEMORY_PATH="$DEFAULT_PATH"
fi

# Expand tilde
MEMORY_PATH="${MEMORY_PATH/#\~/$HOME}"

echo ""
echo -e "${YELLOW}Setting up MemoryCore...${NC}"
echo "  Agent: $AGENT_NAME"
echo "  User: $USER_NAME"
echo "  Path: $MEMORY_PATH"
echo ""

# Create directories
mkdir -p "$MEMORY_PATH/Projects"
mkdir -p "$HOME/.claude"

# Copy memory files
echo "  Copying memory files..."
for file in "$SCRIPT_DIR"/memory/*.md; do
    if [ -f "$file" ]; then
        basename=$(basename "$file")
        sed -e "s/{AGENT_NAME}/$AGENT_NAME/g" \
            -e "s/{USER_NAME}/$USER_NAME/g" \
            -e "s|{MEMORY_PATH}|$MEMORY_PATH|g" \
            "$file" > "$MEMORY_PATH/$basename"
    fi
done

# Copy project template
if [ -f "$SCRIPT_DIR/memory/Projects/_template.md" ]; then
    sed -e "s/{AGENT_NAME}/$AGENT_NAME/g" \
        -e "s/{USER_NAME}/$USER_NAME/g" \
        "$SCRIPT_DIR/memory/Projects/_template.md" > "$MEMORY_PATH/Projects/_template.md"
fi

# Install CLAUDE.md
echo "  Installing CLAUDE.md..."
sed -e "s/{AGENT_NAME}/$AGENT_NAME/g" \
    -e "s/{USER_NAME}/$USER_NAME/g" \
    -e "s|{MEMORY_PATH}|$MEMORY_PATH|g" \
    "$SCRIPT_DIR/.claude/CLAUDE.md" > "$HOME/.claude/CLAUDE.md"

# Install stats script
echo "  Installing stats script..."
sed -e "s/{AGENT_NAME}/$AGENT_NAME/g" \
    "$SCRIPT_DIR/.claude/agent-stats.py" > "$HOME/.claude/agent-stats.py"
chmod +x "$HOME/.claude/agent-stats.py"

# Create empty project labels
echo "  Creating project labels..."
echo "{}" > "$HOME/.claude/project-labels.json"

echo ""
echo -e "${GREEN}${BOLD}MemoryCore installed successfully!${NC}"
echo ""
echo -e "  Memory location:  ${BOLD}$MEMORY_PATH${NC}"
echo -e "  CLAUDE.md:        ${BOLD}$HOME/.claude/CLAUDE.md${NC}"
echo -e "  Stats script:     ${BOLD}$HOME/.claude/agent-stats.py${NC}"
echo ""
echo -e "${BOLD}Your agent ${CYAN}$AGENT_NAME${NC}${BOLD} is ready.${NC}"
echo ""
echo "  Next steps:"
echo "  1. Open Claude Code in any project"
echo "  2. $AGENT_NAME will introduce itself"
echo "  3. Say '${AGENT_NAME} init' to start a new project"
echo "  4. Say 'show stats' to see usage analytics"
echo ""
echo "  All commands:"
echo "    ${AGENT_NAME} init      — Start new project"
echo "    ${AGENT_NAME} learn     — Learn new tech stack"
echo "    ${AGENT_NAME} deploy    — Deployment recipe"
echo "    ${AGENT_NAME} debug     — Structured debugging"
echo "    ${AGENT_NAME} handoff   — Client delivery"
echo "    ${AGENT_NAME}-Evolve    — Force self-reflection"
echo "    mimic this              — Stack migration"
echo "    show stats              — Usage analytics"
echo "    show guide              — Workflow tips"
echo ""
