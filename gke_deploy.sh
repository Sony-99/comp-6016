#!/bin/bash

# Define the log file path
log_file="/home/sony/comp-project/script_log.txt"

# Log the start of the script
echo "$(date '+%Y-%m-%d %H:%M:%S') - Script started." | tee -a "$log_file"

# Total duration in seconds (24 hours)
total_duration=$((24 * 60 * 60))

# Interval between runs (10 minutes)
interval_duration=$((10 * 60))

# Start time
start_time=$(date +%s)

while [ $(($(date +%s) - start_time)) -lt $total_duration ]; do

    # Measure the time for cluster creation
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Creating GKE cluster..." | tee -a "$log_file"
    gcloud container clusters create my-cluster --zone us-central1-a 2>&1 | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - GKE cluster created in $task_duration seconds." | tee -a "$log_file"
    
    # Measure the time for fetching cluster credentials
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Fetching cluster credentials..." | tee -a "$log_file"
    gcloud container clusters get-credentials my-cluster --zone us-central1-a 2>&1 | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Cluster credentials fetched in $task_duration seconds." | tee -a "$log_file"
    
    # Measure the time for Nginx deployment
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Deploying Nginx application..." | tee -a "$log_file"
    kubectl apply -f https://k8s.io/examples/application/deployment.yaml 2>&1 | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Nginx application deployed in $task_duration seconds." | tee -a "$log_file"
    
    # Measure the time for cluster deletion
    task_start=$(date +%s)
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleting GKE cluster..." | tee -a "$log_file"
    gcloud container clusters delete my-cluster --zone us-central1-a --quiet 2>&1 | tee -a "$log_file"
    task_end=$(date +%s)
    task_duration=$((task_end - task_start))
    echo "$(date '+%Y-%m-%d %H:%M:%S') - GKE cluster deleted in $task_duration seconds." | tee -a "$log_file"

    # Log the end of this run
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Run completed." | tee -a "$log_file"
    
    # Wait for 10 minutes before the next iteration
    sleep $interval_duration
done

# Log when the script completes its 24-hour run
echo "$(date '+%Y-%m-%d %H:%M:%S') - Script completed 24-hour run." | tee -a "$log_file"

