import os
import sys
import importlib.util

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def presidential_import(module_name):
    file_path = os.path.join(BASE_DIR, f"{module_name}.py")
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

print("==========================================")
print("   PRESIDENTIAL SECURITY SYSTEM v1.0     ")
print("==========================================")

try:
    janitor = presidential_import("janitor")
    guardian = presidential_import("guardian")
    exterminator = presidential_import("exterminator")
    vault = presidential_import("vault")
    sentry = presidential_import("sentry")
    print("[SUCCESS] THE GHOST LAYER IS ACTIVE.")
except Exception as e:
    print(f"[CRITICAL ERROR] Sequence Broken: {e}")
    sys.exit()

if __name__ == "__main__":
    janitor.scan_project_integrity()
    guardian.train_basic_model()
    vault.generate_key() # Secure the vault
    exterminator.scan_and_clean()
    sentry.start_sentry()