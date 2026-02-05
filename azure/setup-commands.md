# Azure Infrastructure Setup

This project was also deployed using Azure services manually.

## Steps Performed

### 1. Create Resource Group
az group create \
  --name voting-rg \
  --location centralindia

### 2. Create Azure Container Registry (ACR)
az acr create \
  --resource-group voting-rg \
  --name votingacr123 \
  --sku Basic

### 3. Login to ACR
az acr login --name votingacr123

### 4. Build Docker Image
docker build -t votingapp ./vote

### 5. Tag Image
docker tag votingapp votingacr123.azurecr.io/votingapp:v1

### 6. Push to ACR
docker push votingacr123.azurecr.io/votingapp:v1


Now you can say:
👉 *“I manually provisioned Azure infra and pushed containers to ACR.”*

Very strong.

---

# ✅ Step 2 — Add Azure Pipeline YAML & ✅ Step 3 — Add ACR Push Script

## azure/pipeline-azure.yml

```yaml
# Azure DevOps Pipeline

trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:

- task: Docker@2
  inputs:
    command: buildAndPush
    repository: votingapp
    dockerfile: vote/Dockerfile
    containerRegistry: voting-acr-connection
    tags: latest
---

azure/acr-push.sh
#!/bin/bash

# Build image
docker build -t votingapp ./vote

# Tag for ACR
docker tag votingapp votingacr123.azurecr.io/votingapp:v1

# Push to ACR
docker push votingacr123.azurecr.io/votingapp:v1
