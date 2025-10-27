# Project Template Setup Guide

This repository is a **GitHub template** for Python projects with CI/CD, issue-driven development, and Claude Code integration.

## What's Included

✅ **GitHub Actions CI/CD Pipeline**
- Automated linting (Black, flake8)
- Multi-version Python testing (3.10, 3.11)
- Test artifact uploads
- FFmpeg integration for video processing projects

✅ **Issue-Driven Development Workflow**
- `DEV_PLAN.md` for project planning
- `create_issues.py` script to auto-generate GitHub issues
- Phase-based development structure

✅ **Claude Code Integration**
- `CLAUDE.md` with project guidance for Claude
- Consistent development patterns

✅ **Python Project Structure**
- Virtual environment setup
- Requirements management
- Source and test directories
- Automated setup script

## How to Use This Template

### Step 1: Create a New Repository from Template

1. Go to: https://github.com/woolnerd/lightwave
2. Click the green **"Use this template"** button
3. Choose **"Create a new repository"**
4. Name your new project
5. Clone your new repository locally

### Step 2: Customize Your New Project

Run the bootstrap script to customize the template for your project:

```bash
cd your-new-project
./bootstrap.sh
```

The script will prompt you for:
- Project name
- Project description
- Python version requirements
- Whether you need FFmpeg (video processing)
- Additional dependencies

### Step 3: Update Your Development Plan

1. Edit `DEV_PLAN.md` with your project's roadmap
2. Break down work into phases and issues
3. Run `python3 create_issues.py --dry-run` to preview
4. Run `python3 create_issues.py` to create GitHub issues

### Step 4: Configure Claude Code

1. Update `CLAUDE.md` with project-specific guidance
2. Add architecture details
3. Document key commands and workflows
4. Add any special instructions for Claude

### Step 5: Start Development

```bash
# Set up environment
./setup.sh

# Verify CI/CD
git add .
git commit -m "Initial project setup"
git push

# Check GitHub Actions to see CI running
```

## What to Customize

### Required Changes
- [ ] `README.md` - Update project name, description, and goals
- [ ] `DEV_PLAN.md` - Replace with your project plan
- [ ] `CLAUDE.md` - Update project overview and architecture
- [ ] `requirements.txt` - Add your project dependencies

### Optional Changes
- [ ] `.github/workflows/ci.yml` - Adjust Python versions, test commands
- [ ] `setup.sh` - Modify environment setup steps
- [ ] `src/` - Replace placeholder modules with your code
- [ ] `tests/` - Update test structure for your project

### Files to Delete (If Not Needed)
- [ ] `TEMPLATE_SETUP.md` (this file)
- [ ] `bootstrap.sh` (after running it once)
- [ ] `src/frame_extractor.py` (video-specific, not needed for all projects)
- [ ] `tests/test_frame_extraction.py` (video-specific)
- [ ] `docs/FFMPEG_USAGE.md` (if not using FFmpeg)

## Template Features You Can Keep

### CI/CD Pipeline
The GitHub Actions workflow is generic and works for most Python projects. You may want to:
- Adjust Python versions in the test matrix
- Add more linting tools
- Customize test commands
- Add deployment steps

### Issue Generation
The `create_issues.py` script works with any `DEV_PLAN.md` format:
```markdown
### Issue 1.1: Your Issue Title
**Labels**: phase-1, feature
**Estimate**: 2 hours

Your issue description here...
```

### Project Structure
```
your-project/
├── .github/workflows/    # CI/CD pipelines
├── src/                 # Source code
├── tests/               # Tests
├── data/                # Data files (gitignored)
├── output/              # Generated outputs (gitignored)
├── docs/                # Documentation
├── DEV_PLAN.md         # Development roadmap
├── CLAUDE.md           # Claude Code guidance
├── create_issues.py    # Issue automation
└── setup.sh            # Environment setup
```

## Making This Repository a Template

If you're maintaining this template:

1. Go to repository Settings
2. Check **"Template repository"** under General
3. Update this file as needed
4. Push changes - all future projects will get updates

## Tips

- **Keep the template minimal**: Only include what 90% of projects need
- **Document everything**: Future you will thank you
- **Test the template**: Create a test project from it occasionally
- **Version your template**: Tag releases (v1.0, v2.0, etc.)

## Support

For issues with the template itself:
- Create an issue in the template repository
- PRs welcome for improvements!

For issues with your project:
- Use your project's issue tracker
- Claude Code can help with debugging
