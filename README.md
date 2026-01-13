```markdown
# Automated MLOps Training Pipeline

![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=flat-square&logo=docker)
![AWS](https://img.shields.io/badge/AWS-S3-orange?style=flat-square&logo=amazon-aws)
![MLOps](https://img.shields.io/badge/MLOps-Pipeline-green?style=flat-square)

## 📖 Project Overview
This project implements a **Reproducible MLOps Training Pipeline**. 
Unlike traditional scripts that run on a Data Scientist's laptop, this project containerizes the training logic to ensure it runs consistently in any environment (Local, CI/CD, or Cloud).

It automatically performs the following steps:
1.  **Environment Setup:** Installs dependencies inside a clean Docker container.
2.  **Resource Check:** Detects if GPU acceleration (NVIDIA) is available.
3.  **Training:** Simulates a model training job (Housing Price Predictor).
4.  **Validation:** Fails the pipeline if model accuracy is below a threshold (60%).
5.  **Artifact Management:** Automatically versions and uploads the trained model (`.pkl`) to an **AWS S3 Model Registry**.

## 🏗 Architecture
The pipeline follows the "Train-Validate-Register" pattern used in enterprise AI teams.

![MLOps Architecture Diagram](architecture-diagram.png)
*(Note: Generate this diagram using the Mermaid code below)*

## ⚙️ Technical Highlights
* **Containerization:** The `Dockerfile` ensures the training environment is identical every time, eliminating "it works on my machine" issues.
* **Model Registry:** Uses AWS S3 as a centralized storage for model artifacts, allowing for version control of binary files.
* **Automated Validation:** Implements "Gatekeeping" logic—if the model performs poorly, it is rejected before reaching the registry.
* **Hardware Awareness:** The script dynamically detects hardware availability (`os.environ`) to switch between CPU and GPU modes.

## 💻 Usage

### 1. Prerequisites
* Docker installed.
* AWS Credentials configured (for S3 upload).
* An existing S3 bucket.

### 2. Build the Training Container
```bash
docker build -t ml-training-job .

```

### 3. Run the Pipeline (Local Simulation)

We pass AWS credentials into the container so it can authenticate with the Model Registry (S3).

```bash
docker run \
  -e AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id) \
  -e AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key) \
  -e AWS_DEFAULT_REGION=ca-central-1 \
  ml-training-job

```

### 4. Expected Output

```text
Checking for GPU...
⚠️ No GPU detected. Training on CPU (Slow).
Loading data...
Training model...
✅ Training complete! Accuracy: 85%
⬆️ Uploading model to S3: s3://your-bucket-name/models/housing-predictor/v1/model.pkl
✅ Upload Successful! MLOps Cycle Complete.

```

## 🧠 Key Concepts Learned

* **Reproducibility:** Locking dependencies in Docker.
* **Artifact Management:** Separating code (Git) from binary models (S3).
* **CI/CD for ML:** Understanding that data changes trigger pipelines just like code changes do.

```

***
