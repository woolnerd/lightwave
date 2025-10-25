"""
Frame extraction module for extracting frames from video files using FFmpeg.

This module provides utilities to extract frames from video files at various
frame rates and intervals for further processing.
"""

import os
import subprocess
from pathlib import Path
from typing import Optional, Union


def extract_frames(
    video_path: Union[str, Path],
    output_dir: Union[str, Path],
    fps: Optional[float] = 1.0,
    output_format: str = "jpg",
    quality: int = 2,
) -> dict:
    """
    Extract frames from a video file using FFmpeg.

    Args:
        video_path: Path to the input video file
        output_dir: Directory where extracted frames will be saved
        fps: Frame rate for extraction (frames per second). Default is 1.0 (1 frame per second)
        output_format: Output image format (jpg, png, etc.). Default is jpg
        quality: JPEG quality (2-31, lower is better). Default is 2

    Returns:
        dict: Information about the extraction including:
            - success: bool indicating if extraction succeeded
            - output_dir: path to output directory
            - frame_count: number of frames extracted
            - command: the ffmpeg command used

    Raises:
        FileNotFoundError: If video file doesn't exist
        subprocess.CalledProcessError: If ffmpeg command fails
    """
    video_path = Path(video_path)
    output_dir = Path(output_dir)

    # Validate input video exists
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate output filename pattern
    output_pattern = output_dir / f"frame_%04d.{output_format}"

    # Build ffmpeg command
    # -i: input file
    # -vf fps=N: extract N frames per second
    # -q:v: quality for JPEG (2 is high quality)
    command = [
        "ffmpeg",
        "-i",
        str(video_path),
        "-vf",
        f"fps={fps}",
        "-q:v",
        str(quality),
        str(output_pattern),
    ]

    try:
        # Run ffmpeg command
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )

        # Count extracted frames
        frame_files = list(output_dir.glob(f"frame_*.{output_format}"))
        frame_count = len(frame_files)

        return {
            "success": True,
            "output_dir": str(output_dir),
            "frame_count": frame_count,
            "command": " ".join(command),
            "fps": fps,
        }

    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": str(e),
            "stderr": e.stderr,
            "command": " ".join(command),
        }


def get_video_info(video_path: Union[str, Path]) -> dict:
    """
    Get information about a video file using ffprobe.

    Args:
        video_path: Path to the video file

    Returns:
        dict: Video information including duration, fps, resolution, etc.
    """
    video_path = Path(video_path)

    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    # Use ffprobe to get video information
    command = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,r_frame_rate,duration",
        "-of",
        "default=noprint_wrappers=1",
        str(video_path),
    ]

    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )

        # Parse the output
        info = {}
        for line in result.stdout.strip().split("\n"):
            if "=" in line:
                key, value = line.split("=", 1)
                info[key] = value

        return {
            "success": True,
            "width": info.get("width", "unknown"),
            "height": info.get("height", "unknown"),
            "fps": info.get("r_frame_rate", "unknown"),
            "duration": info.get("duration", "unknown"),
        }

    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": str(e),
            "stderr": e.stderr,
        }


if __name__ == "__main__":
    # Example usage
    print("Frame Extractor Module")
    print("=" * 50)
    print("\nThis module provides frame extraction utilities.")
    print("\nExample usage:")
    print("""
from frame_extractor import extract_frames, get_video_info

# Get video info
info = get_video_info('path/to/video.mp4')
print(info)

# Extract frames at 1 fps
result = extract_frames(
    video_path='path/to/video.mp4',
    output_dir='output/frames',
    fps=1.0
)
print(f"Extracted {result['frame_count']} frames")
    """)
