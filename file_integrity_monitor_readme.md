# File Integrity Monitor

A simple Python tool to monitor files in a directory for unauthorized changes. It calculates and stores file hashes, then detects and reports any modifications, additions, or deletions.

## Features
- Monitor a specified directory for file changes
- Optionally include all subdirectories
- Detects and reports:
  - Modified files
  - New (added) files
  - Deleted files
- Simple command-line interface
- Baseline is automatically initialized on first run

## Usage

### 1. Install Requirements
No external dependencies are required (uses Python standard library).

### 2. Run the Monitor
```
python file_integrity_monitor.py <directory> [--recursive]
```
- `<directory>`: Path to the directory you want to monitor
- `--recursive`: (Optional) Include all subdirectories

#### Example: Monitor a folder (non-recursive)
```
python file_integrity_monitor.py C:\Users\YourName\Documents
```

#### Example: Monitor a folder and all subfolders
```
python file_integrity_monitor.py C:\Users\YourName\Documents --recursive
```

## How It Works
- On first run, the tool creates a `hashes.json` file with the hashes of all files in the target directory.
- On subsequent runs, it compares the current state to the baseline and reports any changes.

## Resetting the Baseline
To reset the baseline, delete the `hashes.json` file and rerun the tool.

## Notes
- This tool is for educational and monitoring purposes. For critical systems, use a professional solution.
- Works on Windows, macOS, and Linux (Python 3.6+).
