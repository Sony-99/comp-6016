import pandas as pd

# Load the CSV file
data = pd.read_csv('/home/sony/comp-project/script_log2.csv')

# Define the task columns
tasks = ['Cluster Creation', 'Increase Node Count', 'Fetch Credentials', 'Deploy App', 'Reduce Node Count', 'Delete Cluster']

# Dictionary to store outliers for each task
outliers = {}

# Identify outliers for each task using the IQR method
for task in tasks:
    Q1 = data[task].quantile(0.25)
    Q3 = data[task].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Collecting outliers
    outliers[task] = data[(data[task] < lower_bound) | (data[task] > upper_bound)][['Run Number', task]]

# Print outliers for each task
for task in tasks:
    print(f"\nOutliers for {task}:")
    print(outliers[task])

