# 🚀 DevOps Project: Automated CI/CD Pipeline with GKE & Cloud Build

---

# Project Overview

This project demonstrates an automated **CI/CD pipeline** to build, package, and deploy a containerized **Python Flask** application on **Google Kubernetes Engine (GKE)** using **Google Cloud Build** and **Artifact Registry**.

It reflects real-world **DevOps practices** by automating the entire software delivery process—from code changes to production deployment—ensuring speed, reliability, and scalability.

---
## 🛠 Tech Stack

- ☁️ **GCP Cloud Build**
- 📦 **GCP Artifact Registry**
- ☸️ **Kubernetes Engine (GKE)**
- 🐳 **Docker**
- 🌐 **GitHub**
- 🐍 **Python Flask**

---
## 🔗 Project Workflow

### 1️⃣ Code & Containerize
- Create a **GitHub** repository.
- Develop the **Python Flask** application and dockerize it.
- Build and test the Docker image locally and Push code to GitHub.
---

### 2️⃣ Continuous Integration (CI) with Cloud Build
- Create a **Cloud Build Trigger** connected to the GitHub repository.
- Create cloudbuild.yaml file to automated build docker image and upload docke image to artifact registry.
  
✅ This step automates image creation and ensures consistency across deployments.

---

### 3️⃣ Continuous Deployment (CD) to GKE
- Set up a **GKE Standard Cluster** on **Google Cloud**.
- In GKE:
  - Create a **namespace** for the application.
  - Write **Deployment** and **Service** YAML manifests.
  - Configure **Cloud Build** to automatically deploy to GKE after building the Docker image.

✅ Every new image is deployed to Kubernetes automatically without manual steps.

---

### 4️⃣ Expose the Application
- Extend the **Service YAML** to expose the application using **LoadBalancer** or **Ingress**.
- The application is available through an external endpoint.

✅ The CI/CD pipeline is now fully automated from code to production.

---

## 🔄 CI/CD Flow Summary
GitHub → Cloud Build Trigger → Build Docker Image → Artifact Registry → Cloud Build Deployment → GKE → Service Exposure → Users

---

This project mirrors how modern organizations implement **DevOps and CI/CD** to achieve faster, safer, and more scalable software delivery.
