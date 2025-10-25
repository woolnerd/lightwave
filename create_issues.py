#!/usr/bin/env python3
"""
Script to parse DEV_PLAN.md and create GitHub issues using the GitHub CLI.

Usage:
    python create_issues.py [--dry-run]
"""

import re
import subprocess
import sys
import json


def parse_dev_plan(file_path='DEV_PLAN.md'):
    """Parse the development plan markdown file and extract issues."""

    with open(file_path, 'r') as f:
        content = f.read()

    issues = []
    current_issue = None

    # Split by lines for processing
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Match issue headers like "### Issue 1.1: Title"
        issue_match = re.match(r'^###\s+Issue\s+([\d.]+):\s+(.+)$', line)

        if issue_match:
            # Save previous issue if exists
            if current_issue:
                issues.append(current_issue)

            # Start new issue
            issue_number = issue_match.group(1)
            issue_title = issue_match.group(2)

            current_issue = {
                'number': issue_number,
                'title': f"[{issue_number}] {issue_title}",
                'body': [],
                'labels': [],
                'estimate': None
            }

            i += 1
            continue

        # If we're inside an issue, collect its content
        if current_issue:
            # Match labels line
            labels_match = re.match(r'^\*\*Labels\*\*:\s+(.+)$', line)
            if labels_match:
                labels_str = labels_match.group(1)
                current_issue['labels'] = [label.strip() for label in labels_str.split(',')]
                i += 1
                continue

            # Match estimate line
            estimate_match = re.match(r'^\*\*Estimate\*\*:\s+(.+)$', line)
            if estimate_match:
                current_issue['estimate'] = estimate_match.group(1)
                i += 1
                continue

            # Stop collecting body when we hit the next issue or section
            if line.startswith('###') or line.startswith('---') or line.startswith('##'):
                i += 1
                continue

            # Collect body content
            if line.strip():  # Skip empty lines at the start
                current_issue['body'].append(line)

        i += 1

    # Don't forget the last issue
    if current_issue:
        issues.append(current_issue)

    return issues


def format_issue_body(issue):
    """Format the issue body with metadata."""
    body_lines = issue['body']

    # Add estimate to body if present
    if issue['estimate']:
        body_lines.append(f"\n**Estimated Time**: {issue['estimate']}")

    # Add reference to dev plan
    body_lines.append(f"\n---\n*This issue was generated from DEV_PLAN.md*")

    return '\n'.join(body_lines)


def create_github_issue(issue, dry_run=False):
    """Create a GitHub issue using the gh CLI."""

    title = issue['title']
    body = format_issue_body(issue)
    labels = issue['labels']

    if dry_run:
        print(f"\n{'='*60}")
        print(f"ISSUE: {title}")
        print(f"Labels: {', '.join(labels)}")
        print(f"{'='*60}")
        print(body)
        print(f"{'='*60}\n")
        return True

    # Build gh command
    cmd = ['gh', 'issue', 'create', '--title', title, '--body', body]

    # Add labels
    for label in labels:
        cmd.extend(['--label', label])

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ Created: {title}")
        print(f"  URL: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to create: {title}")
        print(f"  Error: {e.stderr}")
        return False


def main():
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("DRY RUN MODE - No issues will be created\n")

    print("Parsing DEV_PLAN.md...")
    issues = parse_dev_plan()

    print(f"Found {len(issues)} issues to create\n")

    if not dry_run:
        response = input("Create these issues on GitHub? (y/n): ")
        if response.lower() != 'y':
            print("Cancelled.")
            return

    print("\nCreating issues...\n")

    success_count = 0
    for issue in issues:
        if create_github_issue(issue, dry_run):
            success_count += 1

    print(f"\n{'='*60}")
    if dry_run:
        print(f"DRY RUN: Would have created {success_count}/{len(issues)} issues")
    else:
        print(f"Successfully created {success_count}/{len(issues)} issues")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
