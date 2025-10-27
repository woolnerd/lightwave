#!/bin/bash

# Bootstrap script for customizing the project template
# Run this after creating a new repository from the template

set -e

echo "=========================================="
echo "Project Template Bootstrap"
echo "=========================================="
echo ""

# Get project information
read -p "Project name (e.g., my-awesome-project): " PROJECT_NAME
read -p "Project description: " PROJECT_DESC
read -p "Python version (default: 3.11): " PYTHON_VERSION
PYTHON_VERSION=${PYTHON_VERSION:-3.11}

read -p "Does this project need FFmpeg? (y/n): " NEEDS_FFMPEG
read -p "GitHub username/org (for README): " GITHUB_USER
read -p "Author name: " AUTHOR_NAME

echo ""
echo "Configuration:"
echo "  Project: $PROJECT_NAME"
echo "  Description: $PROJECT_DESC"
echo "  Python: $PYTHON_VERSION"
echo "  FFmpeg: $NEEDS_FFMPEG"
echo "  GitHub: $GITHUB_USER"
echo "  Author: $AUTHOR_NAME"
echo ""
read -p "Proceed with setup? (y/n): " CONFIRM

if [ "$CONFIRM" != "y" ]; then
    echo "Setup cancelled."
    exit 1
fi

echo ""
echo "Setting up project..."

# Update README.md
echo "📝 Updating README.md..."
cat > README.md << EOF
# ${PROJECT_NAME}

${PROJECT_DESC}

## Setup

### Prerequisites

- Python ${PYTHON_VERSION} or higher
$(if [ "$NEEDS_FFMPEG" = "y" ]; then echo "- FFmpeg (for video processing)"; fi)
- Git

### Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/${GITHUB_USER}/${PROJECT_NAME}.git
cd ${PROJECT_NAME}

# Run setup script
./setup.sh
\`\`\`

## Development Workflow

This project uses an issue-driven development workflow:

1. Plan your work in \`DEV_PLAN.md\`
2. Generate GitHub issues: \`python3 create_issues.py\`
3. Work through issues with Claude Code
4. CI/CD runs automatically on push

## Project Structure

\`\`\`
${PROJECT_NAME}/
├── .github/workflows/    # CI/CD pipelines
├── src/                 # Source code
├── tests/               # Tests
├── data/                # Data files
├── output/              # Generated outputs
├── docs/                # Documentation
├── DEV_PLAN.md         # Development roadmap
├── CLAUDE.md           # Claude Code guidance
└── requirements.txt    # Python dependencies
\`\`\`

## Testing

\`\`\`bash
# Run tests
pytest tests/

# Run linting
black --check src/ tests/
flake8 src/ tests/
\`\`\`

## CI/CD

GitHub Actions runs automatically on:
- Push to main/develop branches
- Pull requests

The pipeline includes:
- Code formatting checks (Black)
- Linting (flake8)
- Tests on Python ${PYTHON_VERSION}

## Contributing

1. Create a branch for your feature
2. Make changes and test locally
3. Push and create a pull request
4. Wait for CI to pass
5. Request review

## License

MIT

## Author

${AUTHOR_NAME}
EOF

# Update CLAUDE.md
echo "📝 Updating CLAUDE.md..."
cat > CLAUDE.md << EOF
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

${PROJECT_NAME}: ${PROJECT_DESC}

**Tech Stack**: Python ${PYTHON_VERSION}$(if [ "$NEEDS_FFMPEG" = "y" ]; then echo ", FFmpeg"; fi)

## Development Workflow

This project uses an **issue-driven development workflow** with Claude Code:

1. **DEV_PLAN.md** contains the complete project roadmap
2. **create_issues.py** parses DEV_PLAN.md and generates GitHub issues via \`gh\` CLI
3. Work through issues sequentially by phase
4. Commits should reference issue numbers and use \`Closes #N\` to auto-close issues

### Working with Issues

To view an issue:
\`\`\`bash
gh issue view <number> --json title,body,labels | python3 -m json.tool
\`\`\`

To regenerate issues after updating DEV_PLAN.md:
\`\`\`bash
python3 create_issues.py --dry-run  # Preview
python3 create_issues.py            # Create
\`\`\`

## Core Commands

### Environment Setup
\`\`\`bash
# Automated setup (creates venv, installs dependencies)
./setup.sh

# Manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

### Testing
\`\`\`bash
# Run tests
pytest tests/

# Run specific test
python3 tests/test_*.py
\`\`\`

## Architecture

### Module Organization

**src/** - Core functionality modules:
- Add your modules here

**tests/** - Test scripts:
- Tests are executable Python scripts that output their own pass/fail results
- Run directly: \`python3 tests/test_*.py\`

**data/** - Project data:
- \`raw/\` - Source data
- \`processed/\` - Processed data

**output/** - Generated results from processing

**docs/** - Documentation

## Important Implementation Details

### Dependencies
- Add key dependencies and their purposes here

### File Naming & Patterns
- Describe your file naming conventions

## Phases & Next Steps

**Phase 1** - Setup:
- Document your phases here

## Success Criteria
- Define what success looks like for this project
EOF

# Update DEV_PLAN.md template
echo "📝 Creating DEV_PLAN.md template..."
cat > DEV_PLAN.md << EOF
# Development Plan: ${PROJECT_NAME}

## Project Overview

${PROJECT_DESC}

## Goals

- Goal 1: [Define your goals]
- Goal 2: [Define your goals]
- Goal 3: [Define your goals]

---

## Phase 1: Setup and Foundation

### Issue 1.1: Initialize Project Structure
**Labels**: phase-1, setup
**Estimate**: 1 hour

- Set up virtual environment
- Configure dependencies in requirements.txt
- Create basic project structure
- Verify setup.sh works

### Issue 1.2: Set Up Initial Testing
**Labels**: phase-1, testing
**Estimate**: 1 hour

- Create basic test structure
- Add sample tests
- Verify tests run in CI/CD

---

## Phase 2: Core Features

### Issue 2.1: [Your Feature Name]
**Labels**: phase-2, feature
**Estimate**: [time estimate]

[Description of what needs to be built]

---

## Phase 3: Testing and Refinement

### Issue 3.1: Integration Testing
**Labels**: phase-3, testing
**Estimate**: 2 hours

- Create integration tests
- Test end-to-end workflows
- Document test coverage

---

## Phase 4: Documentation

### Issue 4.1: API Documentation
**Labels**: phase-4, documentation
**Estimate**: 2 hours

- Document all public APIs
- Add usage examples
- Create user guide

---

## Success Metrics

- [ ] All tests pass
- [ ] CI/CD pipeline green
- [ ] Documentation complete
- [ ] Ready for use
EOF

# Remove template-specific files if not needed
if [ "$NEEDS_FFMPEG" != "y" ]; then
    echo "🗑️  Removing FFmpeg-specific files..."
    rm -f src/frame_extractor.py
    rm -f tests/test_frame_extraction.py
    rm -f docs/FFMPEG_USAGE.md 2>/dev/null || true
fi

# Update .gitignore
echo "📝 Ensuring .gitignore is configured..."
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Data
data/raw/*.mp4
data/raw/*.avi
data/raw/*.mov
data/processed/
output/

# Models
models/*.pth
models/*.pt
models/*.onnx

# OS
.DS_Store
Thumbs.db

# Jupyter
.ipynb_checkpoints/
*.ipynb

# Environment
.env
.env.local
EOF

echo ""
echo "✅ Bootstrap complete!"
echo ""
echo "Next steps:"
echo "1. Review and customize DEV_PLAN.md"
echo "2. Update CLAUDE.md with project-specific details"
echo "3. Run: ./setup.sh"
echo "4. Generate issues: python3 create_issues.py"
echo "5. Start coding!"
echo ""
echo "You can delete bootstrap.sh and TEMPLATE_SETUP.md now."
