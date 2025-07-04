# 🚀 Automated CI/CD Pipeline Project 
---

## Project Overview

This project demonstrates an automated **CI/CD pipeline** to build, package, and deploy a containerized **Python Flask** application on **Google Kubernetes Engine (GKE)** using **Google Cloud Build** and **Artifact Registry**.

It reflects real-world **DevOps practices** by automating the entire software delivery process from code changes to production deployment ensuring speed, reliability, and scalability.

---

## 🛠 Tech Stack

- ☁️ **GCP Cloud Build**
- 📦 **GCP Artifact Registry**
- ☸️ **Kubernetes Engine (GKE)**
- 🐳 **Docker**
- 🌐 **GitHub**

---

## 🔗 Project Workflow

### 1️⃣ Code & Containerize
- Create a **GitHub repo** and develop the **Python Flask** app and **Dockerize** it.
- Build and test the docker image locally then push the code to **GitHub**.

---

### 2️⃣ Cloud Build 
- Create a **Cloud Build Trigger** connected to the GitHub repository.
- Create a `Cloud Build configuration(YAML)` file to:
  - Automated build the Docker image.
  - Push and store the Docker image to **Artifact Registry**.

---

### 3️⃣ Kubernetes Engine (GKE)
- Set up a **GKE Standard Cluster** on **GCP console**.
- In GKE:
  - Create `a namespace` from `Cloud Shell`.
  - Create a deployment/service yaml file `gke.yaml` for K8 deployment.
  - Create `Cloud Build file` to deploy to GKE automatically after building the container image.

---

### 4️⃣ Expose the Application
- Extend the Service in `gke.yaml` to expose the app using a **LoadBalancer**.
- The application can access via an external endpoint.

✅ This completes the fully automated pipeline from **code to production**.

---

## 🔗 Project Structure
```
gcp-devops-project/
├── app.py                   # Flask application source code
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker image for Flask app
├── cloudbuild.yaml          # Cloud Build configuration file (CI/CD)
├── gke.yaml                 # Kubernetes deployment manifest
└── README.md                # Project documentation
```
---

#### 🔄 CI/CD Flow Summary

GitHub → Cloud Build Trigger → Build Docker Image → Artifact Registry → Cloud Build Deployment → GKE → Service Exposure → Users

---
This project mirrors how modern organizations implement **DevOps and CI/CD** to achieve faster, safer, and more scalable software delivery.
