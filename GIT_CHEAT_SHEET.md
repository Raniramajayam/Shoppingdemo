# 🚀 QUICK REFERENCE - GIT COMMANDS CHEAT SHEET

> **Copy-paste reference for every command we'll learn**

---

## SETUP (One-time)

```powershell
# Initialize Git in your project
git init

# Configure your identity (used for every commit)
git config user.email "your-email@example.com"
git config user.name "Your Name"

# Verify configuration
git config --list
```

---

## DAILY WORKFLOW

```powershell
# See what changed
git status

# See exact changes
git diff

# Stage files for commit
git add .                    # Everything
git add conftest.py          # Single file
git add pages/ tests/        # Multiple folders

# Commit to history
git commit -m "Your message"

# View history
git log
git log --oneline            # Compact view
git log --graph --all        # Branch visualization

# Upload to GitHub
git push origin main
```

---

## FIXING MISTAKES

```powershell
# Restore deleted file
git restore conftest.py

# Unstage files (before commit)
git restore --staged conftest.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Create "reverse" commit (safer than reset)
git revert HEAD
```

---

## BRANCHES

```powershell
# List branches
git branch

# Create branch
git branch feature-search

# Switch branch
git checkout feature-search

# Create and switch (shortcut)
git checkout -b feature-search

# Delete branch
git branch -d feature-search

# Merge branch into main
git checkout main
git merge feature-search
```

---

## GITHUB OPERATIONS

```powershell
# Clone a repo from GitHub
git clone https://github.com/username/project.git

# First push to GitHub
git push -u origin main

# Subsequent pushes
git push origin main

# Pull updates from GitHub
git pull origin main
```

---

## INSPECTION

```powershell
# Show commits
git log
git log --oneline
git log --oneline --graph --all

# Show what's different
git diff                     # Working vs staged
git diff --cached            # Staged vs last commit
git diff HEAD~1              # Compare to last commit

# Show one commit
git show <commit-id>

# Show file history
git log conftest.py
```

---

## STEP-BY-STEP FIRST COMMIT

```powershell
# 1. Check status
cd C:\Users\Sivakumar\Documents\demo\shopping-automation
git status

# 2. Stage all files
git add .

# 3. Verify what's staged
git status

# 4. Commit with message
git commit -m "Initial commit: Playwright automation framework

- Page Object Model with base_page
- Test fixtures for browser/context/page
- Pytest markers for smoke/regression
- HTML reporting with pytest-html
- GitHub Actions workflow setup
- Environment configuration via config.py
- Test data structure
- Logging setup"

# 5. View your commit
git log --oneline

# Done! You've made your first commit.
```

---

## EXPLANATION MAPPING

| Command | What It Does | When to Use |
|---------|-------------|-----------|
| `git init` | Creates .git folder | Once per project |
| `git add .` | Stage all changes | Before committing |
| `git commit -m "msg"` | Save to history | After staging |
| `git push` | Upload to GitHub | Share with team |
| `git pull` | Download from GitHub | Get team updates |
| `git log` | View history | Debug what happened |
| `git status` | Show current state | Before every action |
| `git branch` | Manage parallel work | New features |
| `git merge` | Combine branches | Feature complete |

---

## NEXT STEPS

1. ✅ **STEP 1 (Done)**: Initialize Git & create `.gitignore`
2. **STEP 2 (Next)**: First commit - Stage & commit all files
3. **STEP 3 (Later)**: Push to GitHub
4. **STEP 4 (Later)**: GitHub Actions workflow explained
5. **STEP 5 onwards**: CI/CD integration


