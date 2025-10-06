# Tree of Code - Git Branching Tutorial Memory

## Project Overview

**Purpose**: A simple Python calculator application designed specifically for learning Git branching workflows, version control, and multi-product development strategies.

**Created**: 2025-10-05

**Learning Goals**:
- Master Git branching strategies
- Understand commits, branches, and tags
- Practice feature development workflows
- Learn merge conflict resolution
- Manage multiple product lines (terminal vs GUI)

## Current Project State

### Branch Structure (Strategy 3: Separate Product Branches)

```
main (original/integration branch)
├── terminal (v1.3.0 - terminal calculator product line)
│   └── Features: Add, Subtract, Multiply
└── gui (v1.2.0 - GUI calculator product line)
    └── Features: Add, Subtract (PyQt5)
```

### Active Branches

**Main Product Branches:**
- `main` - Original branch, terminal calculator with add only
- `terminal` - Terminal calculator product line (currently v1.3.0)
- `gui` - GUI (PyQt5) calculator product line (currently v1.2.0)

**Feature Branches:**
- `feature/terminal-multiply` - Added multiply to terminal (merged to terminal)
- `feature/gui-subtract` - Added subtract to GUI (merged to gui)
- `feature/gui` - OLD, can be deleted (replaced by `gui` branch)
- `feature/subtract-terminal` - OLD, merged to main

### Version Tags

**Terminal Product Line:**
- `terminal-v1.2.0` - Terminal with add + subtract
- `terminal-v1.3.0` - Terminal with add + subtract + multiply (CURRENT - needs final tag push)

**GUI Product Line:**
- `gui-v1.1.0` - GUI with add only
- `gui-v1.2.0` - GUI with add + subtract (CURRENT)

### Files

**Code:**
- `calculator.py` - Main calculator application (changes based on branch)
  - On `terminal` branch: Terminal-based calculator
  - On `gui` branch: PyQt5 GUI calculator
- `requirements.txt` - Python dependencies (PyQt5>=5.15.0)
- `README.md` - Project documentation
- `MEMORY.md` - This file

**Environment:**
- `venv/` - Python virtual environment (in .gitignore)
- `.git/` - Git repository data
- `.gitignore` - Excludes venv and other non-tracked files

## Feature Comparison

| Feature | Terminal Branch | GUI Branch |
|---------|----------------|------------|
| Addition | ✅ v1.0 | ✅ v1.1.0 |
| Subtraction | ✅ v1.2.0 | ✅ v1.2.0 |
| Multiplication | ✅ v1.3.0 | ❌ Coming soon |
| Division | ❌ Coming soon | ❌ Coming soon |
| Interface | Terminal/CLI | PyQt5 GUI |

## Key Concepts Learned

### Git Mental Model

**Commits:**
- Each commit is a snapshot that links BACK to its parent
- Commits form a graph structure (Directed Acyclic Graph - DAG)
- Each commit (except the first) has at least one parent
- Merge commits have TWO parents

**Branches:**
- Branches are **movable pointers** to commits
- They move forward with each new commit
- NOT folders containing commits
- Just bookmarks in the commit graph

**Tags:**
- Tags are **permanent labels** on specific commits
- Globally unique across the entire repository (not per-branch)
- Used for marking releases/versions
- Don't move when new commits are made

**Mental Model Shift:**
```
❌ OLD: Branches as folders containing commits
✅ NEW: Branches as pointers to commits in a shared graph

        A ← B ← C ← D ← E
                    ↑   ↑
                  v1.2  main (moves)
                  (tag) (branch)
```

### Branching Strategies Explored

**Strategy 3 (Current)**: Separate Product Branches
- `main` = integration/experimental
- `terminal` = v1.x terminal product line
- `gui` = v2.x GUI product line
- Feature branches branch from product lines
- Merge features back to appropriate product line

### Workflow Patterns Practiced

**Feature Development:**
1. Checkout product branch (`terminal` or `gui`)
2. Create feature branch (`feature/name`)
3. Develop and test
4. Commit changes
5. Merge back to product branch
6. Tag version
7. Push to origin

**Branch Naming Convention:**
- `feature/` - New features
- `bugfix/` or `fix/` - Bug fixes
- `hotfix/` - Urgent production fixes
- The `/` is just part of the name (not a folder structure)

## Tools & Setup

### Development Environment

**Python Virtual Environment:**
```bash
# Activate venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run terminal calculator
python calculator.py
```

**Dependencies:**
- PyQt5>=5.15.0 (for GUI calculator only)

### Git Visualization Tools Used

**GitKraken** (Recommended but paid ~$40-90/year):
- Beautiful visual graph
- Drag-and-drop branch operations
- Easy tagging and merging
- Makes "cultivating the repository" visual and intuitive

**VS Code Git Graph Extension** (Free):
- Install from VS Code extensions
- Shows commit graph visually
- Good for visualization, use terminal for operations

**Built-in Git:**
```bash
# View commit graph in terminal
git log --oneline --graph --all --decorate

# List branches
git branch -a

# List tags
git tag -l

# View current branch
git status
```

## Important Git Commands Reference

### Branching
```bash
git branch                    # List local branches
git branch -a                 # List all branches (local + remote)
git checkout branch-name      # Switch to branch
git checkout -b new-branch    # Create and switch to new branch
git branch branch-name        # Create branch (don't switch)
git branch -d branch-name     # Delete local branch
```

### Merging
```bash
git merge branch-name         # Merge branch into current branch
git merge --abort             # Abort a merge with conflicts
```

### Tagging
```bash
git tag -l                                    # List all tags
git tag -a v1.0.0 -m "Description"           # Create annotated tag
git push origin tag-name                      # Push tag to remote
git tag -d tag-name                          # Delete local tag
git push origin :refs/tags/tag-name          # Delete remote tag
git tag new-tag old-tag^{}                   # Copy tag to new name
```

### Remote Operations
```bash
git push origin branch-name              # Push branch
git push -u origin branch-name           # Push and set upstream
git push origin --delete branch-name     # Delete remote branch
git remote -v                            # List remotes
```

### Status & History
```bash
git status                               # Current branch and changes
git log --oneline --graph --all         # Visual commit history
git show tag-name                        # Show tag details
```

## Session History

### 2025-10-05 - Initial Setup & Learning Session

**What We Built:**
1. ✅ Created virtual environment
2. ✅ Built terminal calculator (v1.0 - addition only)
3. ✅ Converted to PyQt5 GUI calculator (feature/gui branch)
4. ✅ Added subtraction to terminal (v1.2.0)
5. ✅ Restructured to Strategy 3 (separate product branches)
6. ✅ Added subtraction to GUI (v1.2.0)
7. ✅ Added multiplication to terminal (v1.3.0)
8. ✅ Fixed tag naming (gui-v1.x.0, terminal-v1.x.0)

**Key Learning Moments:**
- Discovered PyQt5 not "uninstalled" when switching branches (venv is branch-independent)
- Watched VS Code instantly update files when switching branches
- Saw merge bring changes back ("pop" the changes returned)
- Understood tags are globally unique (not per-branch)
- Visualized Git graph in GitKraken - "cultivating the repository"
- Grasped that commits link BACK to parents, branches are movable pointers

**Current Status:**
- On `terminal` branch
- Just merged `feature/terminal-multiply`
- Need to push `terminal-v1.3.0` tag (tag created, needs push)

## Next Steps / TODO

### Immediate (Resume Session Here)

**Complete Current Task:**
```bash
# Push the terminal-v1.3.0 tag
git push origin terminal-v1.3.0
```

### Planned Learning Exercises

**#3 - Merge Conflicts (NEXT):**
- Goal: Learn how to handle merge conflicts
- Scenario: Modify same code in both `terminal` and `gui` branches
- Then attempt to merge and resolve conflicts
- Demonstrates real-world conflict resolution

**Future Practice Scenarios:**
- Hotfix workflow (urgent bug fix on production)
- Cherry-picking commits between branches
- Rebasing vs merging
- Pull request workflow on GitHub
- Multiple developers working simultaneously

### Potential Feature Additions

**Terminal Calculator:**
- [ ] Add division (v1.4.0)
- [ ] Add modulo operation
- [ ] Add decimal precision handling
- [ ] Add history of calculations

**GUI Calculator:**
- [ ] Port multiply from terminal (v1.3.0)
- [ ] Port division when available (v1.4.0)
- [ ] Add keyboard shortcuts
- [ ] Add calculation history panel
- [ ] Improve error handling UI

## Common Pitfalls & Solutions

### Issue: "PyQt5 not found" error
**Cause:** Virtual environment not activated
**Solution:**
```bash
source venv/bin/activate
# Should see (venv) in prompt
```

### Issue: Tag already exists
**Cause:** Tag names must be globally unique
**Solution:** Use product-specific prefixes (gui-v1.0.0, terminal-v1.0.0)

### Issue: Changes disappeared when switching branches
**Cause:** This is normal! Git switches to that branch's snapshot
**Solution:** This is expected behavior - changes are safe on the other branch

### Issue: Terminal session ended, can't type
**Cause:** Shell exited (typo or Ctrl+D)
**Solution:** Open new terminal tab/window

## Repository Information

**Location:** `/Users/scottnovis/dev/treeofcode`
**Remote:** https://github.com/snovis/treeofcode.git
**Origin:** `origin` = shorthand for the GitHub remote URL

## Design Decisions

**Why Two Product Lines?**
- Demonstrates real-world scenario: legacy terminal app + modern GUI rewrite
- Terminal team can continue adding features
- GUI team can catch up at their own pace
- Eventually could become separate repos

**Why This Calculator?**
- Simple enough to understand quickly
- Complex enough to need version control
- Easy to add features (operations)
- Clear visual difference (terminal vs GUI)
- Perfect for demonstrating branching strategies

## Additional Resources

**Git Concepts:**
- Commits are snapshots with parent links
- Branches are movable pointers
- Tags are permanent labels
- Origin is the remote repository nickname

**Visualization:**
- GitKraken: Premium visual tool ($40-90/year)
- Git Graph (VS Code): Free extension
- `git log --graph`: Built-in terminal visualization

## Notes for Future Sessions

**Remember:**
- Always `source venv/bin/activate` in new terminal sessions
- Check current branch with `git status` or `git branch`
- Tags are global - use prefixes for multiple product lines
- GitKraken makes the graph structure visible and intuitive
- Virtual environment persists across branch switches
- Branch names with `/` are just naming conventions

**Project Philosophy:**
This is a learning sandbox - experiment freely! The whole point is to practice branching, merging, and version control in a safe environment.
