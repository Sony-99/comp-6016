#!/bin/bash

# Define the log file paths
log_file="/home/sony/comp-project/script_log2.txt"
deployment_file="/home/sony/comp-project/flask-deployment.yaml"

# Log the start of the script
echo "$(date '+%Y-%m-%d %H:%M:%S') - Script started." | tee -a "$log_file"

# Record the start time
start_time=$(date +%s)

# Run for 12 hours (43200 seconds)
end_time=$((start_time + 43200))

run_number=0

while [[ $(date +%s) -lt $end_time ]]; do
    run_number=$((run_number + 1))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Starting run #$run_number" | tee -a "$log_file"

    # Measure the time for cluster creation
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Creating GKE cluster with 2 nodes..." | tee -a "$log_file"
    gcloud container clusters create my-cluster --zone us-central1-a --num-nodes=2 2>&1 | grep -vE "Default change:|Note:" | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - GKE cluster created with 2 nodes in $task_duration seconds." | tee -a "$log_file"

    # Increase the number of nodes to 3
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Increasing node count to 3..." | tee -a "$log_file"
    gcloud container clusters resize my-cluster --zone us-central1-a --num-nodes=3 --quiet 2>&1 | grep -vE "Default change:|Note:" | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Node count increased to 3 in $task_duration seconds." | tee -a "$log_file"

    # Fetch cluster credentials
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Fetching cluster credentials..." | tee -a "$log_file"
    gcloud container clusters get-credentials my-cluster --zone us-central1-a 2>&1 | grep -vE "Default change:|Note:" | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Cluster credentials fetched in $task_duration seconds." | tee -a "$log_file"

    # Deploy the Python Flask app using the YAML file
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Deploying Python Flask application..." | tee -a "$log_file"
    kubectl apply -f "$deployment_file" 2>&1 | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Python Flask application deployed in $task_duration seconds." | tee -a "$log_file"

    # Decrease the number of nodes back to 2
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Reducing node count back to 2..." | tee -a "$log_file"
    gcloud container clusters resize my-cluster --zone us-central1-a --num-nodes=2 --quiet 2>&1 | grep -vE "Default change:|Note:" | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Node count reduced back to 2 in $task_duration seconds." | tee -a "$log_file"

    # Delete the GKE cluster
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleting GKE cluster..." | tee -a "$log_file"
    gcloud container clusters delete my-cluster --zone us-central1-a --quiet 2>&1 | grep -vE "Default change:|Note:" | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - GKE cluster deleted in $task_duration seconds." | tee -a "$log_file"

    # Log the end of the run
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Completed run #$run_number." | tee -a "$log_file"
done

# Log when the script completes
echo "$(date '+%Y-%m-%d %H:%M:%S') - Script completed after 12 hours." | tee -a "$log_file"

