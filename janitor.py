import os
import hashlib
import datetime

# Define paths relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "logs", "integrity_audit.log")

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Ensure logs folder exists
    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.makedirs(os.path.dirname(LOG_FILE))
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def calculate_sha256(filepath):
    """Generates a unique fingerprint for a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        return str(e)

def scan_project_integrity():
    print("--- LAYER 2 ACTIVE: JANITOR INTEGRITY SCAN ---")
    # We watch our own core files for tampering
    files_to_watch = ["main.py", "sentry.py"]
    
    for file_name in files_to_watch:
        path = os.path.join(BASE_DIR, file_name)
        if os.path.exists(path):
            file_hash = calculate_sha256(path)
            # We show the first 16 characters of the fingerprint
            print(f"[VERIFIED] {file_name}: {file_hash[:16]}...")
            log_event(f"INTEGRITY CHECK: {file_name} PASSED. HASH: {file_hash}")
        else:
            print(f"[!!!] ALERT: {file_name} IS MISSING!")
            log_event(f"SECURITY ALERT: {file_name} NOT FOUND.")

if __name__ == "__main__":
    scan_project_integrity()