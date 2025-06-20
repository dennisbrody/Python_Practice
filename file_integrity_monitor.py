import os
import hashlib
import json
import argparse

HASHES_FILE = 'hashes.json'

def calculate_file_hash(filepath):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Error hashing {filepath}: {e}")
        return None

def traverse_directory(directory, recursive=False):
    """Yield file paths in a directory, optionally recursively."""
    if recursive:
        for root, _, files in os.walk(directory):
            for file in files:
                yield os.path.join(root, file)
    else:
        for file in os.listdir(directory):
            path = os.path.join(directory, file)
            if os.path.isfile(path):
                yield path

def load_hashes():
    if os.path.exists(HASHES_FILE):
        with open(HASHES_FILE, 'r') as f:
            return json.load(f)
    return None

def save_hashes(hashes):
    with open(HASHES_FILE, 'w') as f:
        json.dump(hashes, f, indent=2)

def get_current_hashes(directory, recursive):
    hashes = {}
    for filepath in traverse_directory(directory, recursive):
        file_hash = calculate_file_hash(filepath)
        if file_hash:
            hashes[os.path.abspath(filepath)] = file_hash
    return hashes

def report_changes(baseline, current):
    baseline_files = set(baseline.keys())
    current_files = set(current.keys())

    added = current_files - baseline_files
    deleted = baseline_files - current_files
    modified = {f for f in baseline_files & current_files if baseline[f] != current[f]}

    if not (added or deleted or modified):
        print("No changes detected.")
        return

    if added:
        print("Added files:")
        for f in added:
            print(f"  + {f}")
    if deleted:
        print("Deleted files:")
        for f in deleted:
            print(f"  - {f}")
    if modified:
        print("Modified files:")
        for f in modified:
            print(f"  * {f}")

def main():
    parser = argparse.ArgumentParser(description='File Integrity Monitor')
    parser.add_argument('directory', help='Directory to monitor')
    parser.add_argument('--recursive', action='store_true', help='Include subdirectories')
    args = parser.parse_args()

    print(f"Monitoring directory: {args.directory}")
    if args.recursive:
        print("Including subdirectories.")
    else:
        print("Not including subdirectories.")

    current_hashes = get_current_hashes(args.directory, args.recursive)
    baseline = load_hashes()
    if baseline is None:
        print("No baseline found. Initializing baseline hashes...")
        save_hashes(current_hashes)
        print(f"Baseline saved to {HASHES_FILE}.")
    else:
        print(f"Loaded baseline from {HASHES_FILE}. Checking for changes...")
        report_changes(baseline, current_hashes)

if __name__ == '__main__':
    main() 