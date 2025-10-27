# Quick Start Guide

## Using This Template (First Time)

```bash
# 1. On GitHub: Click "Use this template" → Create new repository

# 2. Clone your new project
git clone https://github.com/YOUR_USERNAME/YOUR_NEW_PROJECT.git
cd YOUR_NEW_PROJECT

# 3. Customize the project
./bootstrap.sh
# Answer the prompts (project name, description, etc.)

# 4. Set up development environment
./setup.sh

# 5. Update your development plan
# Edit DEV_PLAN.md with your project roadmap

# 6. Generate GitHub issues from your plan
python3 create_issues.py --dry-run  # Preview
python3 create_issues.py            # Create

# 7. Start developing!
git add .
git commit -m "Initial project setup from template"
git push
```

## Daily Development Workflow

```bash
# 1. Check your issues
gh issue list

# 2. Pick an issue and work on it
gh issue view 1

# 3. Make changes, test locally
pytest tests/

# 4. Commit and push (CI runs automatically)
git add .
git commit -m "Closes #1: Implemented feature X"
git push

# 5. Check CI status on GitHub
# Green checkmark = good to merge!
```

## Working with Claude Code

```bash
# Claude Code reads CLAUDE.md for project context
# Just ask Claude to work on your issues:

"Let's work on issue #1"
"Help me implement the feature from issue #3"
"Review the code for issue #5"
```

## Project Structure

```
your-project/
├── .github/workflows/ci.yml  # CI/CD automation
├── src/                      # Your source code
├── tests/                    # Your tests
├── data/                     # Data files (gitignored)
├── output/                   # Generated outputs (gitignored)
├── DEV_PLAN.md              # Your development roadmap
├── CLAUDE.md                # Claude Code guidance
├── create_issues.py         # Issue generation script
├── setup.sh                 # Environment setup
├── bootstrap.sh             # Template customization (run once)
└── requirements.txt         # Python dependencies
```

## Common Commands

```bash
# Environment
./setup.sh                    # Set up virtual environment
source venv/bin/activate      # Activate venv
pip install -r requirements.txt

# Testing
pytest tests/                 # Run all tests
python tests/test_*.py        # Run specific test

# Linting
black src/ tests/             # Format code
flake8 src/ tests/            # Lint code

# Issues
python3 create_issues.py      # Generate from DEV_PLAN.md
gh issue list                 # List all issues
gh issue view 1               # View issue #1
```

## CI/CD

Every push triggers:
1. ✅ Code formatting check (Black)
2. ✅ Linting (flake8)
3. ✅ Tests on Python 3.10 and 3.11
4. ✅ Test artifacts uploaded

Check status: GitHub Actions tab in your repo

## Need Help?

- 📖 Full guide: See `TEMPLATE_SETUP.md`
- 🔧 Template setup: See `GITHUB_TEMPLATE_SETUP.md`
- 💬 Claude Code: Just ask in natural language!
- 🐛 Issues: Use GitHub issues in your project
