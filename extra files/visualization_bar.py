import pandas as pd
import plotly.graph_objs as go

# Load the CSV file
data = pd.read_csv('/home/sony/comp-project/script_log2.csv')

# Define the task columns
tasks = ['Cluster Creation', 'Increase Node Count', 'Deploy App', 'Reduce Node Count', 'Delete Cluster']

# Filter out values greater than 1500 for all task columns
for task in tasks:
    data = data[data[task] <= 1500]

# Create a bar chart
fig_bar = go.Figure()

# Create a bar for each task
for task in tasks:
    fig_bar.add_trace(go.Bar(
        x=data['Run Number'],
        y=data[task],
        name=task,
        hovertemplate=f'Run Number: {{x}}<br>{task}: {{y}} seconds<extra></extra>',
    ))

# Customize the layout for the bar chart
fig_bar.update_layout(
    title='Task Duration Over Runs (Bar Chart)',
    xaxis_title='Run Number',
    yaxis_title='Time (seconds)',
    barmode='group',  # Group bars together
    template='plotly_dark',
    legend_title_text='Tasks',
    xaxis=dict(
        autorange=True,  # Allow the x-axis to auto range
        showgrid=True,   # Show grid lines for better visibility
        zeroline=True,   # Show the zero line
    ),
    yaxis=dict(
        autorange=True,  # Allow the y-axis to auto range
        showgrid=True,   # Show grid lines for better visibility
        zeroline=True,   # Show the zero line
    ),
    dragmode='zoom'   # Enable zooming with the mouse
)

# Show the plot
fig_bar.show()

# Optional: Export the graph to an HTML file for sharing or viewing in a browser
fig_bar.write_html("/home/sony/comp-project/bar_chart_visualization.html", include_plotlyjs='cdn')

