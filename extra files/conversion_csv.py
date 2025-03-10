import re
import csv

# Define the log file path and output CSV path
log_file_path = "/home/sony/comp-project/script_log2.txt"
csv_output_path = "/home/sony/comp-project/script_log2.csv"

# Regular expressions to match each task in the log file
task_patterns = {
    "Cluster Creation": r"GKE cluster created with 2 nodes in (\d+) seconds.",
    "Increase Node Count": r"Node count increased to 3 in (\d+) seconds.",
    "Fetch Credentials": r"Cluster credentials fetched in (\d+) seconds.",
    "Deploy App": r"Python Flask application deployed in (\d+) seconds.",
    "Reduce Node Count": r"Node count reduced back to 2 in (\d+) seconds.",
    "Delete Cluster": r"GKE cluster deleted in (\d+) seconds.",
}

# List to hold the parsed log data
log_data = []

with open(log_file_path, "r") as log_file:
    run_number = 0
    run_data = {}
    
    for line in log_file:
        if "Starting run" in line:
            run_number += 1
            run_data = {"Run Number": run_number}
        elif "Completed run" in line:
            log_data.append(run_data)
        else:
            for task, pattern in task_patterns.items():
                match = re.search(pattern, line)
                if match:
                    run_data[task] = match.group(1)  # Duration in seconds

# Write the extracted data to CSV
with open(csv_output_path, "w", newline="") as csv_file:
    fieldnames = ["Run Number", "Cluster Creation", "Increase Node Count", 
                  "Fetch Credentials", "Deploy App", "Reduce Node Count", "Delete Cluster"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(log_data)

print(f"Log data has been successfully written to {csv_output_path}")
