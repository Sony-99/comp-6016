import pandas as pd

# Define the file paths
log_file_path = '/home/sony/comp-project/script_log.txt'
csv_file_path = '/home/sony/comp-project/script_log.csv'

# Read the existing CSV data
existing_data = pd.read_csv(csv_file_path)

# Read the new log data from the text file
# Assuming the structure is similar to the CSV (Run Number, Timestamp, Cluster Creation, Fetch Credentials, Deploy App, Delete Cluster)
new_data = []

with open(log_file_path, 'r') as f:
    for line in f:
        # Split the line into its components assuming it's tab-separated like the CSV
        parts = line.strip().split('\t')
        
        # Ensure that the line has the expected number of parts (6 columns)
        if len(parts) == len(existing_data.columns):
            new_data.append(parts)

# Convert new data into a DataFrame
new_data_df = pd.DataFrame(new_data, columns=existing_data.columns)

# Convert 'Timestamp' to datetime if needed
new_data_df['Timestamp'] = pd.to_datetime(new_data_df['Timestamp'])

# Concatenate the existing data with the new data
combined_data = pd.concat([existing_data, new_data_df], ignore_index=True)

# Remove duplicates if any (based on 'Run Number' or 'Timestamp', adjust as needed)
combined_data.drop_duplicates(subset=['Run Number', 'Timestamp'], keep='last', inplace=True)

# Save the updated data back to CSV
combined_data.to_csv(csv_file_path, index=False)

print("CSV file updated successfully!")
