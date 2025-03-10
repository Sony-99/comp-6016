#!/bin/bash

# Define input log file and output CSV file paths
log_file="/home/sony/comp-project/script_log.txt"
csv_file="/home/sony/comp-project/script_log.csv"

# Write CSV header
echo "Timestamp,Task,Duration (seconds)" > "$csv_file"

# Extract and organize data from the log file
while IFS= read -r line; do
    if [[ "$line" == *"Script started"* ]]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S'),Script started," >> "$csv_file"
    elif [[ "$line" == *"Creating GKE cluster..."* ]]; then
        start_time=$(echo "$line" | cut -d' ' -f1-2)
    elif [[ "$line" == *"GKE cluster created in"* ]]; then
        task="Creating GKE cluster"
        duration=$(echo "$line" | grep -oP '[0-9]+(?= seconds)')
        echo "$start_time,$task,$duration" >> "$csv_file"
    elif [[ "$line" == *"Fetching cluster credentials..."* ]]; then
        start_time=$(echo "$line" | cut -d' ' -f1-2)
    elif [[ "$line" == *"Cluster credentials fetched in"* ]]; then
        task="Fetching cluster credentials"
        duration=$(echo "$line" | grep -oP '[0-9]+(?= seconds)')
        echo "$start_time,$task,$duration" >> "$csv_file"
    elif [[ "$line" == *"Deploying Nginx application..."* ]]; then
        start_time=$(echo "$line" | cut -d' ' -f1-2)
    elif [[ "$line" == *"Nginx application deployed in"* ]]; then
        task="Deploying Nginx application"
        duration=$(echo "$line" | grep -oP '[0-9]+(?= seconds)')
        echo "$start_time,$task,$duration" >> "$csv_file"
    elif [[ "$line" == *"Deleting GKE cluster..."* ]]; then
        start_time=$(echo "$line" | cut -d' ' -f1-2)
    elif [[ "$line" == *"GKE cluster deleted in"* ]]; then
        task="Deleting GKE cluster"
        duration=$(echo "$line" | grep -oP '[0-9]+(?= seconds)')
        echo "$start_time,$task,$duration" >> "$csv_file"
    elif [[ "$line" == *"Run completed"* ]]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S'),Run completed," >> "$csv_file"
    fi
done < "$log_file"

echo "Log file successfully converted to CSV format: $csv_file"
