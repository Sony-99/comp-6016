**Understanding the Performance Variability of Modern Cloud Services**

**Overview**

This repository contains the research artifacts for the project
**\"Understanding the Performance Variability in Modern Cloud
Services.\"** The study focuses on evaluating the performance
variability of managed Kubernetes services: **Azure Kubernetes Service
(AKS) and Google Kubernetes Engine (GKE).**

**Research Objective**

While Kubernetes is widely adopted for container orchestration, its
performance variability over prolonged use remains underexplored. This
study conducts a comparative analysis of AKS and GKE by measuring key
performance metrics at both the **node and cluster levels** under
varying workloads. The insights from this research aim to help
organizations optimize their Kubernetes deployments for long-term use.

**Experiments**

The study consists of **two primary experiments:**

**Experiment 1: Baseline Performance Analysis**

-   **Workload 1**: Lightweight web application from Azure's official
    documentation for AKS.

**Experiment 2: Dynamic Node Scaling**

-   **Scaling Up**: Nodes are increased to simulate growing resource
    demands.

-   **Scaling Down**: Nodes are reduced to assess resource deallocation
    behavior.

-   **Cluster Deletion**: Ensures no residual cloud resources are left
    after each cycle.

**How to Use This Repository**

**1. Clone the Repository**

git clone https://github.com/YourUsername/comp-6016.git

cd comp-6016

**2. Running the Experiments**

Each experiment contains shell scripts to automate the deployment,
monitoring, and teardown of Kubernetes clusters.

**Running Experiment 1**

cd comp-6016

bash gke_deploy.sh

**Running Experiment 2**

cd comp-6016

bash gke_deploy2.sh

**3. Analyzing the Results**

-   There are .csv files for each experiment that contains recorded
    performance metrics.

-   There are .py files for each experiment that includes Python scripts
    for data analysis.

python simple_visualization.py

python new_visualization.py

**Dependencies**

To run the experiments and analyze results, ensure you have the
following installed:

-   **Google Cloud SDK** (for GKE management)

-   **Azure CLI** (for AKS management)

-   **kubectl** (to interact with Kubernetes clusters)

-   **Python 3.x** (for visualization scripts)

-   **Pandas & Matplotlib** (for data analysis)

**Contributors**

-   **Sony Maharjan**

-   **Shovan Tuladhar**
