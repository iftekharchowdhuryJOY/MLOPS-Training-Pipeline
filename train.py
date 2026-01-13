import sys
import pickle
import random
import boto3
import os

# --- CONFIGURATION ---
BUCKET_NAME = "iftekhar-tf-state-2026"
S3_KEY = "models/housing-predictor/v1/model.pkl"

def train():
    print("--- MLOps Pipeline Started ---")
    
    # 1. Simulate GPU Check (Your Job as DevOps is to make this say "Yes")
    # In a real library like PyTorch, this would be: torch.cuda.is_available()
    print("Checking for GPU...")
    if os.environ.get('NVIDIA_VISIBLE_DEVICES'):
        print("✅ GPU Detected! Training will be fast.")
    else:
        print("⚠️ No GPU detected. Training on CPU (Slow).")

    # 2. Simulate Training
    print("Loading data...")
    print("Training model...")
    accuracy = random.randint(70, 99)
    
    if accuracy < 60:
        print(f"❌ Accuracy too low ({accuracy}%), failing job.")
        sys.exit(1)
        
    print(f"✅ Training complete! Accuracy: {accuracy}%")
    
    # 3. Save to Local File
    model_content = {"version": "1.0", "accuracy": accuracy}
    local_file = "model.pkl"
    with open(local_file, "wb") as f:
        pickle.dump(model_content, f)
        
    # 4. Upload to S3 (The Registry)
    print(f"⬆️ Uploading model to S3: s3://{BUCKET_NAME}/{S3_KEY}")
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, BUCKET_NAME, S3_KEY)
        print("✅ Upload Successful! MLOps Cycle Complete.")
    except Exception as e:
        print(f"❌ Upload Failed: {str(e)}")
        # Check credentials if this fails!
        sys.exit(1)

if __name__ == "__main__":
    train()