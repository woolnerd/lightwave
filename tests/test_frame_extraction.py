"""
Test script for frame extraction functionality.

This script:
1. Generates a simple test video using FFmpeg
2. Tests frame extraction at different frame rates (1fps, 5fps)
3. Validates the extraction results
"""

import sys
import subprocess
from pathlib import Path

# Add parent directory to path to import our module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from frame_extractor import extract_frames, get_video_info


def generate_test_video(output_path: Path, duration: int = 10):
    """
    Generate a simple test video using FFmpeg.

    Args:
        output_path: Where to save the test video
        duration: Duration in seconds
    """
    print(f"Generating test video: {output_path}")

    # Create a test video with a color gradient and timer
    # This creates a 10-second video at 30fps with 1280x720 resolution
    command = [
        "ffmpeg",
        "-f",
        "lavfi",
        "-i",
        f"testsrc=duration={duration}:size=1280x720:rate=30",
        "-pix_fmt",
        "yuv420p",
        "-y",  # Overwrite output file
        str(output_path),
    ]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"✓ Test video generated: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to generate test video: {e.stderr}")
        return False


def test_frame_extraction():
    """Test frame extraction at different frame rates."""

    # Setup paths
    test_dir = Path(__file__).parent
    data_dir = test_dir.parent / "data" / "raw"
    output_base = test_dir.parent / "output"

    data_dir.mkdir(parents=True, exist_ok=True)
    output_base.mkdir(parents=True, exist_ok=True)

    test_video = data_dir / "test_video.mp4"

    print("=" * 60)
    print("FFmpeg Frame Extraction Test")
    print("=" * 60)

    # Generate test video
    if not test_video.exists():
        if not generate_test_video(test_video, duration=10):
            print("Failed to generate test video. Exiting.")
            return False

    print(f"\nTest video: {test_video}")

    # Get video information
    print("\n--- Video Information ---")
    info = get_video_info(test_video)
    if info["success"]:
        print(f"✓ Resolution: {info['width']}x{info['height']}")
        print(f"✓ FPS: {info['fps']}")
        print(f"✓ Duration: {info['duration']} seconds")
    else:
        print(f"✗ Failed to get video info: {info.get('error')}")
        return False

    # Test 1: Extract frames at 1 fps
    print("\n--- Test 1: Extract frames at 1 fps ---")
    output_1fps = output_base / "frames_1fps"
    result_1fps = extract_frames(video_path=test_video, output_dir=output_1fps, fps=1.0)

    if result_1fps["success"]:
        print(f"✓ Extracted {result_1fps['frame_count']} frames")
        print(f"✓ Output directory: {result_1fps['output_dir']}")
        print(f"✓ Command: {result_1fps['command']}")
        # For a 10-second video at 1fps, we should get ~10 frames
        expected_frames = 10
        if abs(result_1fps["frame_count"] - expected_frames) <= 2:
            print(f"✓ Frame count is as expected (~{expected_frames} frames)")
        else:
            print(
                f"⚠ Warning: Expected ~{expected_frames} frames, got {result_1fps['frame_count']}"
            )
    else:
        print(f"✗ Failed: {result_1fps.get('error')}")
        print(f"✗ stderr: {result_1fps.get('stderr')}")
        return False

    # Test 2: Extract frames at 5 fps
    print("\n--- Test 2: Extract frames at 5 fps ---")
    output_5fps = output_base / "frames_5fps"
    result_5fps = extract_frames(video_path=test_video, output_dir=output_5fps, fps=5.0)

    if result_5fps["success"]:
        print(f"✓ Extracted {result_5fps['frame_count']} frames")
        print(f"✓ Output directory: {result_5fps['output_dir']}")
        print(f"✓ Command: {result_5fps['command']}")
        # For a 10-second video at 5fps, we should get ~50 frames
        expected_frames = 50
        if abs(result_5fps["frame_count"] - expected_frames) <= 5:
            print(f"✓ Frame count is as expected (~{expected_frames} frames)")
        else:
            print(
                f"⚠ Warning: Expected ~{expected_frames} frames, got {result_5fps['frame_count']}"
            )
    else:
        print(f"✗ Failed: {result_5fps.get('error')}")
        print(f"✗ stderr: {result_5fps.get('stderr')}")
        return False

    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"✓ Video generation: SUCCESS")
    print(f"✓ Video info extraction: SUCCESS")
    print(f"✓ Frame extraction (1fps): SUCCESS - {result_1fps['frame_count']} frames")
    print(f"✓ Frame extraction (5fps): SUCCESS - {result_5fps['frame_count']} frames")
    print("\n✓ All tests passed!")
    print("=" * 60)

    return True


if __name__ == "__main__":
    success = test_frame_extraction()
    sys.exit(0 if success else 1)
