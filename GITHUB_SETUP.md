# GitHub Setup Guide

## 🚀 Setting Up Your Structural Engineering Notebooks on GitHub

### Step 1: Create GitHub Repository

1. **Go to GitHub.com** and sign in
2. **Click "+" → "New repository"**
3. **Repository Settings**:
   - **Name**: `structural-engineering-notebooks`
   - **Description**: `Professional Jupiter notebooks for structural engineering calculations with handcalcs integration`
   - **Visibility**: Public (recommended) or Private
   - **Important**: DO NOT initialize with README, .gitignore, or license

### Step 2: Connect Local Repository

After creating the repository, run these commands in your terminal:

```bash
# Add GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/structural-engineering-notebooks.git

# Push to GitHub
git push -u origin main
```

### Step 3: Verify Upload

Your repository should now contain:
- **Organized notebooks** in `notebooks/beam_design/` and `notebooks/column_design/`
- **Professional scripts** in `scripts/pdf_generators/` and `scripts/utilities/`
- **LaTeX templates** in `templates/`
- **Comprehensive documentation** including README.md, PROJECT_STRUCTURE.md
- **Cursor rules** for professional development standards

### Step 4: Repository Settings (Optional)

1. **Add topics/tags**: `structural-engineering`, `jupyter-notebooks`, `handcalcs`, `concrete-design`, `python`
2. **Enable GitHub Pages** (if you want to host documentation)
3. **Set up branch protection** for the main branch
4. **Add collaborators** if working with a team

### Step 5: Professional Repository Description

Use this suggested description for your GitHub repository:

```
🏗️ Professional structural engineering calculations using Jupiter notebooks with handcalcs integration. 

Features professional LaTeX templates, automated PDF generation, and comprehensive calculation workflows following ACI 318-19 standards.

Built for structural engineers who want beautiful, professional calculation sheets.
```

### Step 6: README Badges (Optional)

Add these badges to make your repository look professional:

```markdown
![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?logo=Jupyter)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
```

### Commands Summary

```bash
# After creating the GitHub repository:
git remote add origin https://github.com/YOUR_USERNAME/structural-engineering-notebooks.git
git push -u origin main

# For future updates:
git add .
git commit -m "Your commit message"
git push
```

### Troubleshooting

If you encounter authentication issues:

1. **Use Personal Access Token** instead of password
2. **Set up SSH keys** for easier authentication
3. **Use GitHub CLI** for simplified authentication

```bash
# Install GitHub CLI and authenticate
gh auth login
```

Your professional structural engineering project is now ready for GitHub! 🎉 