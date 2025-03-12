# Rewards System

This directory contains files related to the progression and reward system for the Sorcery of Code learning platform.

## Structure

- `leaderboard.json` - Tracks all users' progress, keys earned, and badges awarded
- `keys/` - Contains individual key files for users when they complete challenges
- `progress/` - Contains per-user progress tracking files

## How It Works

1. When a user completes a challenge, they submit a pull request with their solution
2. GitHub Actions validates the solution using tests
3. If the solution passes, a unique key is generated and awarded to the user
4. The key is used to unlock the next lesson
5. Progress is recorded in the leaderboard and user-specific files

## Badges

Users can earn badges for completing modules and special challenges:

- `module-0-beginner-review_master` - Completed all lessons in Module 0
- `module-python_master` - Completed all lessons in Module 1
- `module-ml_master` - Completed all lessons in Module 2
- `module-ai-backend_master` - Completed all lessons in Module 3

## Leaderboard

The leaderboard is updated automatically and shows:
- Which users have completed which lessons
- Total badges earned by each user
- Timestamps for completion events 

# Administrator Guide for Sorcery of Code

This guide explains how to manage the two-repository system for Sorcery of Code.

## Repository Architecture

1. **Master Repository (Private)**: Contains all unlocked content
   - Repository: `short-circuits-hi/Sorcery-of-Code-Master`
   - Access: Administrators only

2. **Student Repository (Public)**: Contains only what students have unlocked
   - Repository: `short-circuits-hi/Sorcery-of-Code`
   - Access: Public

## Adding New Content

1. Always add new content to the master repository first
2. Update the module structure in both repositories' scripts
3. Add appropriate tests for new challenges
4. Test the content thoroughly

## Updating the Public Repository

The public repository should only contain:
- The first lesson (unlocked)
- LOCKED.md files for all other lessons
- GitHub Actions workflows for validation
- No sensitive content or solution keys

## Managing Student Progress

Student progress is tracked through:
1. GitHub Actions validating challenge solutions
2. The rewards system in the leaderboard.json file
3. Custom PRs created for each student when they unlock content

## Troubleshooting

If a student reports issues with lesson unlocking:
1. Check their PR history
2. Verify the GitHub Actions logs
3. Manually trigger the unlock process if needed

## Security Considerations

- Never push unlocked content to the public repository
- Regularly audit repository access
- Ensure GitHub secrets are properly configured 