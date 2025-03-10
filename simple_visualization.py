import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Read the CSV file
data = pd.read_csv('/home/sony/comp-project/script_log.csv')

# Convert the 'Timestamp' column to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Define the tasks
tasks = ['Cluster Creation', 'Fetch Credentials', 'Deploy App', 'Delete Cluster']

# Filter out outliers (values > 1200) by replacing them with NaN for the combined plot
for task in tasks:
    data[task] = data[task].apply(lambda x: x if x <= 1200 else None)

# Create the combined graph first
fig_combined = go.Figure()

# Adding each task to the combined plot
for task in tasks:
    fig_combined.add_trace(go.Scatter(
        x=data['Timestamp'], 
        y=data[task],
        mode='lines+markers',
        name=task,
        connectgaps=True  # Ensures the points are joined
    ))

# Updating the layout for combined graph
fig_combined.update_layout(
    title="Task Durations Over Time (Combined)",
    xaxis_title="Time",
    yaxis_title="Duration (seconds)",
    xaxis=dict(
        tickformat='%I %p',  # Display time in hours with AM/PM
        dtick=3600000  # 1 hour interval in milliseconds
    ),
    yaxis=dict(
        range=[0, 1200],  # Limit the y-axis to 1200 seconds for combined graph
        dtick=200  # Interval of 200 seconds on y-axis
    ),
    hovermode="x unified",
    template="plotly_dark"  # Apply dark mode
)

# Create individual graphs for each task
fig_individuals = make_subplots(
    rows=2, cols=2,
    subplot_titles=tasks
)

# Add a trace for each task in individual subplots
for i, task in enumerate(tasks):
    row = i // 2 + 1
    col = i % 2 + 1
    # Filter out outliers only for the combined plot, not the individual ones
    task_data = data[task].dropna()
    
    fig_individuals.add_trace(go.Scatter(
        x=data['Timestamp'], 
        y=data[task],
        mode='lines+markers',
        name=task,
        connectgaps=True  # Ensures the points are joined in individual plots as well
    ), row=row, col=col)

    # Set dynamic y-axis range for each subplot without a fixed dtick
    fig_individuals.update_yaxes(
        range=[0, max(task_data) + 50],  # Set y-axis range dynamically with a small margin
        row=row, col=col
    )

# Update layout for individual task plots
fig_individuals.update_layout(
    title="Task Durations Over Time (Individual)",
    height=800,
    hovermode="x unified",
    template="plotly_dark"  # Apply dark mode to individual graphs as well
)

# Set consistent x-axis formatting for individual subplots
for i in range(1, 3):
    for j in range(1, 3):
        fig_individuals.update_xaxes(
            tickformat='%I %p',  # Display time in hours with AM/PM
            dtick=3600000,  # 1 hour interval
            row=i, col=j
        )

# Show the combined graph and individual subplots
fig_combined.show()
fig_individuals.show()

