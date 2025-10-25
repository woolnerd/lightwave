# Lightwave

A test project exploring video indexing and matching using computer vision as a proof-of-concept for video conforming workflows in film post-production.

## Problem Statement

In film post-production, editors work with low-res proxy files to create a final cut. The "conform" step requires matching these edited segments back to high-res raw source footage. EDL timecodes are often unreliable due to frame rate differences and re-encodes. This project explores using computer vision to perceptually match video segments.

## Tech Stack

- **FFmpeg**: Video processing and frame extraction
- **Hugging Face Models**: Visual embeddings (CLIP or similar)
- **Python**: Primary development language

## Development Workflow

This project demonstrates a workflow for planning and executing development with Claude Code:

### 1. Development Plan → GitHub Issues Workflow

1. **Create Development Plan**: See `DEV_PLAN.md` for the complete project plan broken down into phases and specific issues
2. **Generate GitHub Issues**: Run `python3 create_issues.py` to automatically create GitHub issues from the development plan
3. **Work Through Issues**: Use Claude Code to work through each issue systematically

### 2. Working with Claude Code on Issues

To work on a specific issue with Claude:

```bash
# Reference the issue number in your request
"Let's work on issue #1 - Initialize Python Project Structure"
```

Claude Code can help you:
- Understand the requirements from the issue
- Implement the solution
- Test the changes
- Update the issue status
- Create commits and PRs

## Project Structure

```
lightwave/
├── DEV_PLAN.md          # Complete development plan
├── create_issues.py     # Script to generate GitHub issues from plan
├── README.md           # This file
├── src/                # Source code (to be created)
├── tests/              # Test files (to be created)
├── data/               # Sample data and test videos (to be created)
└── output/             # Generated results (to be created)
```

## Getting Started

The project is currently in the planning phase. To start development:

1. Check the [Issues](https://github.com/woolnerd/lightwave/issues) page for current tasks
2. Issues are labeled by phase (phase-1 through phase-5) and category
3. Start with Phase 1 issues to set up the project infrastructure
4. Work through phases sequentially

## Current Status

- Phase 1: Not started
- Phase 2: Not started
- Phase 3: Not started
- Phase 4: Not started
- Phase 5: Not started

## Contributing

This is a test/learning project, but feel free to explore the issue-driven development workflow demonstrated here.

## License

MIT
