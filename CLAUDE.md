# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Lightwave is a test/proof-of-concept project exploring computer vision-based video conforming for film post-production. The goal is to match edited proxy footage to high-res source files using visual embeddings instead of unreliable EDL timecodes.

**Tech Stack**: Python, FFmpeg, Hugging Face transformers (CLIP or similar), torch/torchvision

## Development Workflow

This project uses an **issue-driven development workflow** with Claude Code:

1. **DEV_PLAN.md** contains the complete project roadmap broken into 5 phases with 14 specific issues
2. **create_issues.py** parses DEV_PLAN.md and generates GitHub issues via `gh` CLI
3. Work through issues sequentially by phase (phase-1 → phase-5)
4. Commits should reference issue numbers and use `Closes #N` to auto-close issues

### Working with Issues

To view an issue:
```bash
gh issue view <number> --json title,body,labels | python3 -m json.tool
```

To regenerate issues after updating DEV_PLAN.md:
```bash
python3 create_issues.py --dry-run  # Preview
python3 create_issues.py            # Create
```

## Core Commands

### Environment Setup
```bash
# Automated setup (creates venv, installs dependencies)
./setup.sh

# Manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Testing
```bash
# Test FFmpeg integration and frame extraction
python3 tests/test_frame_extraction.py
```

### Running Modules
```bash
# Frame extraction (from src/)
python3 -c "from src.frame_extractor import extract_frames, get_video_info; ..."
```

## Architecture

### Data Flow (Planned)
```
Source Videos → Frame Extraction → Visual Embeddings → Index Storage
                     ↓
Master Video → Frame Extraction → Visual Embeddings → Similarity Search → Match Results
```

### Module Organization

**src/** - Core functionality modules:
- `frame_extractor.py`: FFmpeg wrapper for extracting frames and getting video metadata. Uses subprocess to call ffmpeg/ffprobe directly.
  - `extract_frames(video_path, output_dir, fps, ...)` - Extract frames at specified frame rate
  - `get_video_info(video_path)` - Get video metadata (resolution, fps, duration)

**tests/** - Test scripts (not pytest-based, standalone scripts):
- Tests are executable Python scripts that output their own pass/fail results
- Run directly: `python3 tests/test_*.py`

**data/** - Video data:
- `raw/` - Source videos and test videos
- `processed/` - Extracted frames and computed features

**output/** - Generated results from processing

**models/** - Downloaded model weights (e.g., CLIP)

**docs/** - Documentation:
- `FFMPEG_USAGE.md` - Comprehensive FFmpeg reference with commands and Python wrapper usage

## Important Implementation Details

### FFmpeg Integration
- Frame extraction uses subprocess to call ffmpeg directly (not ffmpeg-python library)
- Default extraction: 1fps, JPEG quality=2 (highest), pattern `frame_%04d.jpg`
- Test video generation uses lavfi testsrc filter (30fps, 1280x720, color gradient with timer)
- See docs/FFMPEG_USAGE.md for detailed command reference

### Dependencies
- **torch/transformers**: For future visual embedding generation (Phase 2)
- **ffmpeg-python**: Listed but not yet used (direct subprocess calls instead)
- **numpy/pandas**: For data manipulation
- Dev tools: pytest, black, flake8, jupyter

### File Naming & Patterns
- Extracted frames: `frame_0001.jpg`, `frame_0002.jpg`, etc. (zero-padded 4 digits)
- Module imports: `from src.module_name import ...` (src/ in sys.path)

## Phases & Next Steps

**Phase 1 (Setup)** - Issues #1-2:
- ✓ #1: Project structure, requirements.txt, setup.sh
- ✓ #2: FFmpeg integration with frame extraction

**Phase 2 (Feature Extraction)** - Issues #3-5:
- #3: Enhance frame_extractor.py with batch processing, metadata, logging
- #4: Create feature_extractor.py for CLIP/ViT embeddings
- #5: Create indexer.py for storing embeddings with metadata

**Phase 3 (Matching)** - Issues #6-8:
- Similarity search, master video processing, results visualization

**Phase 4 (Testing)** - Issues #9-11:
- Test dataset creation, end-to-end testing, optimization

**Phase 5 (Documentation)** - Issues #12-14:
- API docs, user guide, future improvements

## Success Criteria
- Index source videos and match master video segments with >80% accuracy
- Process 10 minutes of video in <5 minutes
- Proof-of-concept validates computer vision approach for production
