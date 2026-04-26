import os
import joblib
from sklearn.ensemble import RandomForestClassifier

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "ai_models")
MODEL_PATH = os.path.join(MODEL_DIR, "behavior_brain.pkl")

def train_basic_model():
    """Teaches the AI the difference between 'Safe' and 'Dirt'."""
    print("[AI] Training Behavioral Guardian...")
    
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)

    # Features: [CPU_Usage%, Data_Sent_MB, Hidden_Process(0/1), Access_Camera(0/1)]
    X = [
        [5, 0.1, 0, 0],   # Safe: Low activity
        [95, 800, 1, 1],  # Dirt: High activity, hidden, camera on
        [12, 1.5, 0, 1],  # Safe: Video call
        [88, 1200, 1, 0], # Dirt: Ransomware/Spyware
    ]
    # Labels: 0 = Secure, 1 = Malicious
    y = [0, 1, 0, 1]
    
    clf = RandomForestClassifier(n_estimators=10)
    clf.fit(X, y)
    
    # Save the brain so we don't have to retrain every time
    joblib.dump(clf, MODEL_PATH)
    print(f"[AI] Brain saved to {MODEL_PATH}")

def predict_behavior(stats):
    """Uses the AI to decide if a new behavior is 'Dirt'."""
    if not os.path.exists(MODEL_PATH):
        train_basic_model()
    
    clf = joblib.load(MODEL_PATH)
    prediction = clf.predict([stats])
    return "MALICIOUS" if prediction[0] == 1 else "SECURE"

if __name__ == "__main__":
    train_basic_model()