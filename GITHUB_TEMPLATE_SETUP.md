# How to Make This a GitHub Template Repository

Follow these steps to convert this repository into a reusable GitHub template.

## Step 1: Enable Template Repository Setting

1. Go to your repository on GitHub: `https://github.com/woolnerd/lightwave`
2. Click on **Settings** (top right)
3. Scroll down to the **"Template repository"** section
4. ✅ Check the box **"Template repository"**
5. Click **Save**

That's it! Your repository is now a template.

## Step 2: Test Your Template

1. Go to your repository homepage
2. You should now see a green **"Use this template"** button
3. Click it and create a test repository
4. Clone the test repo and run `./bootstrap.sh`
5. Verify everything works

## Step 3: Maintain Your Template

### Updating the Template

When you improve the template:
```bash
# Make changes to template files
git add .
git commit -m "Improve template: add XYZ"
git push

# Optional: Tag releases
git tag -a v1.0 -m "Template v1.0"
git push --tags
```

All future projects created from the template will get the latest version.

### What to Keep in the Template

✅ **Keep These:**
- `.github/workflows/ci.yml` - CI/CD pipeline
- `create_issues.py` - Issue automation
- `setup.sh` - Environment setup
- `bootstrap.sh` - Project customization script
- `TEMPLATE_SETUP.md` - Usage instructions
- `CLAUDE.md` - Template guidance for Claude
- `DEV_PLAN.md` - Example development plan
- Project structure (src/, tests/, data/, etc.)

❌ **Don't Keep Project-Specific Files:**
- Actual implementation code (unless it's example/starter code)
- Project-specific data files
- Specific issue content (keep the format, not the content)

### Template Best Practices

1. **Keep it minimal**: Only include what 90% of projects need
2. **Document everything**: Assume users are new to the workflow
3. **Test regularly**: Create a test project from the template occasionally
4. **Version control**: Tag stable versions (v1.0, v2.0, etc.)
5. **Gather feedback**: Ask users what's helpful or confusing

## Using Your Template

Once it's set up as a template, anyone (including you) can:

### Create a New Project

1. Go to `https://github.com/woolnerd/lightwave`
2. Click **"Use this template"** → **"Create a new repository"**
3. Name the new project
4. Clone it locally:
   ```bash
   git clone https://github.com/your-username/new-project-name.git
   cd new-project-name
   ```
5. Run the bootstrap script:
   ```bash
   ./bootstrap.sh
   ```
6. Follow the prompts to customize for your project
7. Start developing!

### Quick Start for New Projects

```bash
# On GitHub: Use template to create repo

# Locally:
git clone https://github.com/USERNAME/NEW_PROJECT.git
cd NEW_PROJECT
./bootstrap.sh  # Follow prompts
./setup.sh      # Set up environment
python3 create_issues.py --dry-run  # Preview issues
python3 create_issues.py            # Create issues
```

## Template Features

Your template includes:

### 1. Automated CI/CD
- Linting (Black, flake8)
- Testing on multiple Python versions
- Runs on every push and PR

### 2. Issue-Driven Development
- Plan in `DEV_PLAN.md`
- Auto-generate GitHub issues
- Track progress systematically

### 3. Claude Code Integration
- `CLAUDE.md` provides context
- Consistent development patterns
- AI-assisted development

### 4. Quick Setup
- `setup.sh` for environment
- `bootstrap.sh` for customization
- Virtual environment management

## Sharing Your Template

### Public Template
If your repository is public, anyone can use it:
- Share the URL: `https://github.com/woolnerd/lightwave`
- They click "Use this template"
- Done!

### Private Template
If your repository is private:
- Only people with access can use it
- Useful for company/team templates
- Same process, just requires permissions

### Template Collection
Create multiple templates for different project types:
- `python-ml-template` - Machine learning projects
- `python-web-template` - Web applications
- `python-cli-template` - Command-line tools
- etc.

## Troubleshooting

### "Use this template" button not showing
- Make sure "Template repository" is checked in Settings
- Refresh the page
- Check you're on the repository homepage

### Template not updating for new projects
- New projects get a snapshot at creation time
- They don't auto-update when template changes
- Consider adding an "update from template" workflow

### Bootstrap script not working
- Check file permissions: `chmod +x bootstrap.sh`
- Ensure bash is available
- Check for syntax errors

## Advanced: Template Variables

For more advanced templates, you can use GitHub's template variables:

```markdown
# {{ repository.name }}

Created from template by {{ repository.owner }}
```

These get replaced automatically when creating from template.

## Next Steps

1. ✅ Enable template repository in Settings
2. 📝 Update README to be more template-focused
3. 🧪 Test by creating a project from template
4. 📢 Share with your team
5. 🔄 Iterate based on feedback

## Resources

- [GitHub Template Repositories Documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
- [About repository templates](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
