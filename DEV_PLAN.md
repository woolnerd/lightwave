# Lightwave Development Plan

**Project Goal**: Test project to explore video indexing and matching using computer vision as a proof-of-concept for video conforming workflows.

## Problem Statement
In film post-production, editors work with low-res proxy files and create a final cut. The "conform" step requires matching these edited segments back to high-res raw source footage. EDL timecodes are often unreliable due to frame rate differences and re-encodes. This project explores using computer vision to perceptually match video segments.

## Test Project Scope
Build a simple proof-of-concept that can:
1. Ingest source video files and extract visual features
2. Index those features for fast lookup
3. Take a master video (edited sequence) and find matching segments in indexed sources

## Tech Stack
- **FFmpeg**: Video processing and frame extraction
- **Hugging Face Models**: Visual embeddings (CLIP or similar)
- **Python**: Primary development language
- **Vector DB or simple indexing**: For storing and searching embeddings

---

## Phase 1: Project Setup
**Goal**: Set up development environment and project structure

### Issue 1.1: Initialize Python Project Structure
- [ ] Create virtual environment setup
- [ ] Create requirements.txt with initial dependencies (ffmpeg-python, transformers, torch, pillow)
- [ ] Set up basic directory structure (src/, tests/, data/, output/)
- [ ] Create README.md with setup instructions
- [ ] Add .gitignore for Python projects

**Labels**: setup, phase-1
**Estimate**: 1 hour

### Issue 1.2: Install and Test FFmpeg Integration
- [ ] Verify FFmpeg is installed on system
- [ ] Create basic script to extract frames from a test video
- [ ] Test frame extraction at different intervals (1fps, 5fps)
- [ ] Document FFmpeg commands and python wrapper usage

**Labels**: setup, phase-1, ffmpeg
**Estimate**: 2 hours

---

## Phase 2: Video Ingestion & Feature Extraction
**Goal**: Build pipeline to extract and index visual features from source videos

### Issue 2.1: Frame Extraction Module
- [ ] Create `frame_extractor.py` module
- [ ] Implement function to extract frames at configurable intervals
- [ ] Add support for batch processing multiple videos
- [ ] Save extracted frames with metadata (video source, timestamp, frame number)
- [ ] Add logging and error handling

**Labels**: core, phase-2, ffmpeg
**Estimate**: 3 hours

### Issue 2.2: Visual Feature Extraction with Hugging Face
- [ ] Research and select appropriate model (CLIP, ViT, or similar)
- [ ] Create `feature_extractor.py` module
- [ ] Implement function to generate embeddings from frames
- [ ] Test embedding generation on sample frames
- [ ] Optimize for batch processing (GPU support if available)

**Labels**: core, phase-2, ml, huggingface
**Estimate**: 4 hours

### Issue 2.3: Build Video Index
- [ ] Design index structure (JSON, SQLite, or vector DB)
- [ ] Create `indexer.py` module
- [ ] Implement function to store embeddings with metadata
- [ ] Add ability to load existing index
- [ ] Create index visualization/inspection utility

**Labels**: core, phase-2
**Estimate**: 3 hours

---

## Phase 3: Video Matching & Lookup
**Goal**: Implement search functionality to match master video segments to source footage

### Issue 3.1: Similarity Search Implementation
- [ ] Create `matcher.py` module
- [ ] Implement cosine similarity search function
- [ ] Add support for finding top-N matches
- [ ] Test with sample queries
- [ ] Add confidence threshold tuning

**Labels**: core, phase-3, ml
**Estimate**: 3 hours

### Issue 3.2: Master Video Processing Pipeline
- [ ] Create pipeline to process master/edited video
- [ ] Extract frames from master video
- [ ] Generate embeddings for master frames
- [ ] Match each frame against indexed sources
- [ ] Output match results with timestamps and confidence scores

**Labels**: core, phase-3
**Estimate**: 4 hours

### Issue 3.3: Results Visualization
- [ ] Create output format for match results (JSON, CSV)
- [ ] Build simple visualization showing matched segments
- [ ] Add side-by-side frame comparison utility
- [ ] Generate match report with statistics

**Labels**: core, phase-3, visualization
**Estimate**: 3 hours

---

## Phase 4: Testing & Optimization
**Goal**: Test the system end-to-end and optimize performance

### Issue 4.1: Create Test Dataset
- [ ] Generate or find sample video files (public domain)
- [ ] Create synthetic "edited" video from source clips
- [ ] Document ground truth matches
- [ ] Add test data to repository (or download script)

**Labels**: testing, phase-4
**Estimate**: 2 hours

### Issue 4.2: End-to-End Testing
- [ ] Run complete pipeline on test dataset
- [ ] Measure accuracy of matches
- [ ] Identify edge cases and failure modes
- [ ] Document performance metrics

**Labels**: testing, phase-4
**Estimate**: 3 hours

### Issue 4.3: Performance Optimization
- [ ] Profile code to find bottlenecks
- [ ] Optimize frame extraction (parallel processing)
- [ ] Optimize embedding generation (batch size tuning)
- [ ] Consider caching strategies
- [ ] Document performance improvements

**Labels**: optimization, phase-4
**Estimate**: 4 hours

---

## Phase 5: Documentation & Demo
**Goal**: Create documentation and demo for the proof-of-concept

### Issue 5.1: API Documentation
- [ ] Document all modules and functions
- [ ] Add docstrings to all public methods
- [ ] Create usage examples
- [ ] Generate API documentation (sphinx or similar)

**Labels**: documentation, phase-5
**Estimate**: 2 hours

### Issue 5.2: User Guide & Demo Script
- [ ] Write comprehensive README
- [ ] Create Jupyter notebook demo
- [ ] Add CLI interface for common workflows
- [ ] Record demo video or create visual guide

**Labels**: documentation, phase-5
**Estimate**: 3 hours

### Issue 5.3: Future Improvements Document
- [ ] Document limitations of current approach
- [ ] List potential improvements (better models, scene detection, etc.)
- [ ] Outline path to production system
- [ ] Gather feedback from post-production house

**Labels**: documentation, phase-5
**Estimate**: 2 hours

---

## Success Criteria
- Successfully index a collection of source videos
- Match segments from a master video to source footage with reasonable accuracy (>80%)
- Complete end-to-end pipeline runs in reasonable time (< 5 minutes for 10 minutes of video)
- Clear documentation for setup and usage
- Proof-of-concept validates approach for production development
