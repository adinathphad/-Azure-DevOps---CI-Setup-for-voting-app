# Azure-DevOps---CI-Setup-for-voting-app

Azure DevOps CI setup for a multi-service Dockerized voting application.

This project demonstrates Continuous Integration (CI) by automatically building and validating multiple services on every code push.  
It focuses only on CI (build + validation). Deployment (CD) is NOT included.

---

## 🚀 Tech Stack

- Python (Flask) – Vote Service
- .NET (C#) – Worker Service
- Node.js (Express) – Result Service
- Redis – Message Queue
- PostgreSQL – Database
- Docker & Docker Compose
- Azure DevOps Pipelines
- GitHub Actions

---

## 🧠 Architecture Flow

User → Python Vote App → Redis → .NET Worker → PostgreSQL → Node Result App

- Vote service collects votes
- Redis stores votes temporarily (queue)
- Worker processes votes
- PostgreSQL stores data
- Result service displays counts

---

## 📁 Project Structure

Azure-DevOps---CI-Setup-for-voting-app/

vote/ – Python service  
worker/ – .NET service  
result/ – Node.js service  
db/ – Database scripts  
docker-compose.yml – Orchestration  
.github/workflows/ – GitHub CI  
azure/ – Azure DevOps CI pipelines  

---

## ▶️ Run Locally

Build and start:
docker compose up --build

---

## 🔁 Continuous Integration (CI)

CI runs automatically on every push.

Pipelines perform:

✔ Build Docker images  
✔ Compile services  
✔ Start containers  
✔ Validate application runs  
✔ Detect errors early  

---

## 🟢 GitHub Actions

File:
.github/workflows/ci.yml

Steps:
- Checkout code
- Docker build
- Docker compose up
- Verify containers

---

## 🔵 Azure DevOps Pipelines

Separate CI pipelines:

- python-pipeline.yml
- node-pipeline.yml
- dotnet-pipeline.yml

Each pipeline:
- Builds service
- Builds Docker image
- Validates build success

---

## 🐳 Docker Commands

Build:
docker compose build

Run:
docker compose up

Stop:
docker compose down

---

## Azure Deployment (Manual)

This project was also tested with Azure DevOps:

- Created Resource Group
- Created Azure Container Registry (ACR)
- Built Docker images
- Pushed images to ACR
- Used Azure DevOps pipeline

Commands available in /azure folder.


## 🎯 Concepts Covered

- Microservices architecture
- Multi-language services
- Docker containerization
- Docker Compose orchestration
- Continuous Integration (CI)
- Azure DevOps pipelines
- GitHub Actions automation

---


