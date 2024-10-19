# Git

- Allows us to keep track of changes.
- Synchronizes code between different people.
- Test changes to code without losing access to the original.
- Revert to old versions of our code.

# GitHub

- Stores Git repositories.

# Creating a repository

- Create a new one on GitHub
- copy the url
- run git clone <url> on your terminal
- ls: list files in the directory. you just cloned.
- cd hello to move into the hello directory.

- use touch 'name of file' to create a new file

# Git commands

- git init: initialize repository locally

- git clone <url> add a repo locally from remote

- git add: stage changes

- git commit -m: commit staged changes

- git push: push changes to remote

- git pull: pulls changes from remote to locally

- git commit -am 'commit message': shorthand to stage commit at the same time.
- git log: describes the commits.
- git reset: reverts older state
  - git reset --hard 'commit message'
  - git reset origin/master. (for a commit on the remote)

# Merge Conflicts: when pulling

- Fix conflicts: git merge.

# Branching

- git branch: tells you the current branch and the branches available
- git branch 'name of new branch'
- git checkout -b 'name of new branch': creates new branch and switches to it.
- git branch -d 'name of branch to be deleted': deletes a branch
- git branch -D 'name of branch to be deleted': deletes a branch that we've made changes on.
- git checkout 'name of branch you want to switch to': switch branches.
- git merge 'name of branch to merge to the current branch': merge branches.

\*\* You can use GitHub pages to host your sites.
