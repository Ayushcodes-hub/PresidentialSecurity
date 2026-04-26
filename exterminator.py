import psutil
import os
import sys

# Force-link to our AI Guardian
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

import guardian

def scan_and_clean():
    print("--- LAYER 4 ACTIVE: AUTONOMOUS EXTERMINATOR ---")
    
    # We scan the most active processes
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            # Gather "Behavioral Data" for the AI
            # [CPU%, Mem_MB, Is_Hidden, Has_Camera_Access]
            # (Simplified for this version)
            cpu = proc.info['cpu_percent']
            mem = proc.info['memory_info'].rss / (1024 * 1024)
            is_hidden = 1 if proc.info['name'].startswith('system_') else 0
            
            # Ask the AI for a verdict
            behavior_data = [cpu, mem, is_hidden, 0]
            verdict = guardian.predict_behavior(behavior_data)
            
            if verdict == "MALICIOUS":
                print(f"[!!!] DIRT DETECTED: Killing Process {proc.info['name']} (PID: {proc.info['pid']})")
                # proc.kill() # SHOCK WARNING: We keep this commented out for the first test!
                print(f"[ACTION] Simulation: Process {proc.info['pid']} would be terminated.")
                
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == "__main__":
    scan_and_clean()