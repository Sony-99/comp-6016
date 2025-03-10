import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Load the CSV file with task durations
data = pd.read_csv('/home/sony/comp-project/script_log2.csv')

# Parse the timestamps from the log
timestamps = []
with open('/home/sony/comp-project/script_log2.txt', 'r') as file:
    for line in file:
        if "Starting run" in line:
            timestamp = line.split(' - ')[0]  # Extract timestamp portion before " - "
            timestamps.append(timestamp)

# Ensure the timestamps match the number of runs
data['Timestamp'] = pd.to_datetime(timestamps)

# Define the task columns
tasks = ['Cluster Creation', 'Increase Node Count', 'Fetch Credentials', 'Deploy App', 'Reduce Node Count', 'Delete Cluster']

# Filter out outliers (e.g., values > 1500 seconds for task columns)
for task in tasks:
    data = data[data[task] <= 1500]

### COMBINED GRAPH (Page 1) ###

# Create a combined graph
fig_combined = go.Figure()

# Add each task to the combined plot
for task in tasks:
    fig_combined.add_trace(go.Scatter(
        x=data['Timestamp'],
        y=data[task],
        mode='lines+markers',
        name=task,
        hovertemplate=f'Time: {{x}}<br>{task}: {{y}} seconds<extra></extra>',
        marker=dict(size=8)
    ))

# Customize the layout for the combined graph
fig_combined.update_layout(
    title='Task Duration Over Time (Combined)',
    xaxis_title='Time',
    yaxis_title='Time (seconds)',
    hovermode='closest',
    template='plotly_dark'
)

# Update the x-axis for the combined graph to display time in 12-hour format (e.g., "12 PM", "1 PM")
fig_combined.update_xaxes(
    tickformat='%I %p',  # Format to display hours in 12-hour format with AM/PM
    dtick=3600000,  # 1-hour interval in milliseconds
    range=[data['Timestamp'].min(), data['Timestamp'].max()]
)

# Show the combined plot
fig_combined.show()

# Optional: Export the combined graph to an HTML file
fig_combined.write_html('/home/sony/comp-project/combined_visualization.html', include_plotlyjs='cdn')


### INDIVIDUAL GRAPHS (Page 2, 3x2 Grid) ###

# Create a 3x2 grid for individual task subplots
fig_individuals = make_subplots(
    rows=3, cols=2,  # 3x2 layout for the tasks
    subplot_titles=["Cluster Creation", "Increase Node Count", "Fetch Credentials", "Deploy App", "Reduce Node Count", "Delete Cluster"]
)

# Add each task to the respective position in the grid
for i, task in enumerate(tasks):  # Now plotting all 6 tasks in the grid
    row = i // 2 + 1
    col = i % 2 + 1

    fig_individuals.add_trace(go.Scatter(
        x=data['Timestamp'],
        y=data[task],
        mode='lines+markers',
        name=task,
        hovertemplate=f'Time: {{x}}<br>{task}: {{y}} seconds<extra></extra>',
        marker=dict(size=8)
    ), row=row, col=col)

    # Customize the y-axis for each task's plot
    fig_individuals.update_yaxes(
        title_text="Time (seconds)",
        row=row, col=col
    )

# Customize the layout for individual task plots
fig_individuals.update_layout(
    title='Task Duration Over Time (Individual)',
    hovermode='closest',
    template='plotly_dark',
    height=1200  # Adjust height for 3x2 grid layout
)

# Update the x-axis for each subplot to display time in 12-hour format
for i in range(1, 4):  # 3 rows
    for j in range(1, 3):  # 2 columns
        fig_individuals.update_xaxes(
            tickformat='%I %p',  # Format to display hours in 12-hour format with AM/PM
            dtick=3600000,  # 1-hour interval in milliseconds
            range=[data['Timestamp'].min(), data['Timestamp'].max()],
            row=i, col=j
        )

# Show the individual task plots
fig_individuals.show()

# Optional: Export the individual subplots to an HTML file
fig_individuals.write_html('/home/sony/comp-project/individual_visualization.html', include_plotlyjs='cdn')

