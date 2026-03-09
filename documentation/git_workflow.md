# Git Workflow

The project used Git and GitHub for version control and collaboration.

Workflow Process

1. Each developer worked on their own branch (e.g. muhammad-setup, eman, mahi).
2. Changes were committed locally using:
   git add .
   git commit -m "Description of change"
3. Branches were pushed to GitHub.
4. Branches were periodically merged with main to stay up to date.
5. Merge conflicts were resolved manually when necessary.

Branch Strategy

Main branch:
Contains the stable version of the project.

Feature branches:
Used for development work before merging into main.

Benefits

This workflow allowed:
- safe experimentation
- easier debugging
- collaboration without overwriting each other's work.