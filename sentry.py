from scapy.all import sniff, IP, TCP
import datetime
import os

# This finds the EXACT folder where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "network_audit.log")

# Create the logs folder if it vanished
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log_incident(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        print(f"[ERROR] Could not write to log: {e}")

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        
        # Log every connection for the audit trail
        log_incident(f"TRAFFIC: {ip_src} -> {ip_dst}")
        print(f"[SECURE] Traffic: {ip_src} -> {ip_dst}")

def start_sentry():
    print("--- LAYER 1 ACTIVE: SENTRY NETWORK SHIELD ---")
    print(f"Targeting Log: {LOG_FILE}")
    # Increased to 20 packets to ensure we catch enough data
    sniff(prn=packet_callback, count=20)
    print("--- TEST COMPLETE: CHECK LOGS NOW ---")

if __name__ == "__main__":
    start_sentry()