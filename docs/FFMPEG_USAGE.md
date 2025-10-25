# FFmpeg Usage Guide

This document explains how to use FFmpeg for video processing in the Lightwave project.

## Table of Contents
- [Basic FFmpeg Commands](#basic-ffmpeg-commands)
- [Python Wrapper Usage](#python-wrapper-usage)
- [Common Use Cases](#common-use-cases)

## Basic FFmpeg Commands

### Extract Frames at Specific FPS

Extract 1 frame per second:
```bash
ffmpeg -i input_video.mp4 -vf fps=1 -q:v 2 output/frame_%04d.jpg
```

Extract 5 frames per second:
```bash
ffmpeg -i input_video.mp4 -vf fps=5 -q:v 2 output/frame_%04d.jpg
```

**Parameters:**
- `-i`: Input video file
- `-vf fps=N`: Video filter to extract N frames per second
- `-q:v N`: JPEG quality (2-31, where 2 is highest quality)
- `%04d`: Zero-padded 4-digit frame number (e.g., 0001, 0002, ...)

### Get Video Information

Use `ffprobe` (part of FFmpeg) to get video metadata:
```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate,duration \
  -of default=noprint_wrappers=1 input_video.mp4
```

**Output example:**
```
width=1280
height=720
r_frame_rate=30/1
duration=10.000000
```

### Generate Test Video

Create a test video with color patterns (useful for testing):
```bash
ffmpeg -f lavfi -i testsrc=duration=10:size=1280x720:rate=30 \
  -pix_fmt yuv420p test_video.mp4
```

**Parameters:**
- `duration`: Video length in seconds
- `size`: Resolution (widthxheight)
- `rate`: Frame rate (fps)
- `-pix_fmt yuv420p`: Pixel format for broad compatibility

## Python Wrapper Usage

### Frame Extractor Module

The `frame_extractor.py` module provides a Python interface to FFmpeg:

```python
from src.frame_extractor import extract_frames, get_video_info

# Get video information
info = get_video_info('path/to/video.mp4')
print(f"Resolution: {info['width']}x{info['height']}")
print(f"FPS: {info['fps']}")
print(f"Duration: {info['duration']} seconds")

# Extract frames at 1 fps
result = extract_frames(
    video_path='path/to/video.mp4',
    output_dir='output/frames',
    fps=1.0,
    output_format='jpg',
    quality=2
)

print(f"Extracted {result['frame_count']} frames to {result['output_dir']}")
```

### Function Reference

#### `extract_frames()`

Extracts frames from a video file.

**Parameters:**
- `video_path` (str | Path): Path to input video
- `output_dir` (str | Path): Directory for extracted frames
- `fps` (float, optional): Frame rate for extraction. Default: 1.0
- `output_format` (str, optional): Output format (jpg, png). Default: 'jpg'
- `quality` (int, optional): JPEG quality (2-31, lower is better). Default: 2

**Returns:**
```python
{
    'success': bool,
    'output_dir': str,
    'frame_count': int,
    'command': str,  # The FFmpeg command used
    'fps': float
}
```

#### `get_video_info()`

Gets metadata about a video file.

**Parameters:**
- `video_path` (str | Path): Path to video file

**Returns:**
```python
{
    'success': bool,
    'width': str,
    'height': str,
    'fps': str,
    'duration': str
}
```

## Common Use Cases

### 1. Extract Frames for Visual Analysis

For computer vision tasks, extract frames at a moderate rate:
```python
result = extract_frames(
    video_path='source_footage.mp4',
    output_dir='data/processed/source_frames',
    fps=1.0  # 1 frame per second is often sufficient
)
```

### 2. High-Frequency Sampling

For precise matching or motion analysis:
```python
result = extract_frames(
    video_path='master_edit.mp4',
    output_dir='data/processed/master_frames',
    fps=5.0  # 5 frames per second for better temporal resolution
)
```

### 3. Batch Processing Multiple Videos

```python
from pathlib import Path
from src.frame_extractor import extract_frames

video_dir = Path('data/raw/')
output_base = Path('data/processed/')

for video_file in video_dir.glob('*.mp4'):
    output_dir = output_base / video_file.stem
    result = extract_frames(
        video_path=video_file,
        output_dir=output_dir,
        fps=1.0
    )
    print(f"{video_file.name}: {result['frame_count']} frames")
```

### 4. Quality vs. Storage Trade-off

**High Quality (larger files):**
```python
extract_frames(video_path='input.mp4', output_dir='output', quality=2)
```

**Balanced (recommended):**
```python
extract_frames(video_path='input.mp4', output_dir='output', quality=5)
```

**Lower Quality (smaller files):**
```python
extract_frames(video_path='input.mp4', output_dir='output', quality=10)
```

## Testing

Run the test suite to verify FFmpeg integration:
```bash
python3 tests/test_frame_extraction.py
```

This test will:
1. Generate a 10-second test video
2. Extract frames at 1 fps and 5 fps
3. Verify the frame counts are correct
4. Report success/failure

## Troubleshooting

### FFmpeg not found
```
FileNotFoundError: ffmpeg not found
```
**Solution:** Install FFmpeg:
- macOS: `brew install ffmpeg`
- Ubuntu: `sudo apt-get install ffmpeg`
- Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### Permission denied
```
PermissionError: Cannot write to output directory
```
**Solution:** Ensure the output directory exists and you have write permissions:
```python
Path(output_dir).mkdir(parents=True, exist_ok=True)
```

### Out of disk space
Frame extraction can generate many large files. Monitor disk usage:
```bash
du -sh output/
```

Clean up test frames when done:
```bash
rm -rf output/frames_*
```

## Performance Notes

- **Frame Rate Impact**: Higher FPS = more frames = more storage and processing time
- **Quality Impact**: Lower quality values (2-5) produce larger files but better images
- **Recommended Settings**:
  - Initial indexing: 1 fps, quality 2
  - Precise matching: 5 fps, quality 2
  - Testing/development: 1 fps, quality 5

## Next Steps

After extracting frames, the next phase is to:
1. Generate embeddings from extracted frames (Issue #2.2)
2. Index the embeddings for fast lookup (Issue #2.3)
3. Match frames from master video to source footage (Issue #3.x)
