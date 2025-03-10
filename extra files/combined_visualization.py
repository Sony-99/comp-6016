import pandas as pd
import plotly.graph_objs as go

# Load the CSV file with task durations
csv_file_path = '/home/sony/comp-project/script_log2.csv'
data = pd.read_csv(csv_file_path)

# Parse the timestamps from the log file
log_file_path = '/home/sony/comp-project/script_log2.txt'
timestamps = []
with open(log_file_path, 'r') as file:
    for line in file:
        if "Starting run" in line:
            timestamp = line.split(' - ')[0]
            timestamps.append(timestamp)

# Convert timestamps to datetime
data['Timestamp'] = pd.to_datetime(timestamps)

# Task list
tasks = ['Cluster Creation', 'Increase Node Count', 'Fetch Credentials', 'Deploy App', 'Reduce Node Count', 'Delete Cluster']

# Create the main figure
fig = go.Figure()

# Add each task to the same plot
for task in tasks:
    fig.add_trace(
        go.Scatter(
            x=data['Timestamp'],
            y=data[task],
            mode='lines+markers',
            name=task,
            hovertemplate=f'Time: {{x}}<br>{task}: {{y}} seconds<extra></extra>',
            marker=dict(size=5)
        )
    )

# Update layout with titles and axis labels
fig.update_layout(
    title='Task Duration Over Time (Combined Graph)',
    xaxis_title='Time',
    yaxis_title='Time (seconds)',
    hovermode='closest',
    template='plotly_dark',
)

# Adjust x-axis tick intervals to every hour and format labels
fig.update_xaxes(
    tickformat='%I %p',  # Format as 12pm, 1pm
    dtick=3600000,  # 1-hour interval
    tickangle=45
)

# Save the figure to an HTML file in the same directory
output_file_path = '/home/sony/comp-project/task_duration_combined_graph.html'  # Same directory
fig.write_html(output_file_path)

print(f"Graph saved to {output_file_path}")

