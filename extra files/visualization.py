import pandas as pd
import plotly.graph_objs as go

# Load the CSV file
data = pd.read_csv('/home/sony/comp-project/script_log2.csv')

# Define the task columns
tasks = ['Cluster Creation', 'Increase Node Count', 'Deploy App', 'Reduce Node Count', 'Delete Cluster']

# Filter out values greater than 1500 for all task columns
for task in tasks:
    data = data[data[task] <= 1500]

# Create an interactive plot for each task
fig = go.Figure()

for task in tasks:
    fig.add_trace(go.Scatter(
        x=data['Run Number'],
        y=data[task],
        mode='lines+markers',
        name=task,
        hovertemplate=f'Run Number: {{x}}<br>{task}: {{y}} seconds<extra></extra>',
        marker=dict(size=8)
    ))

# Customize the layout
fig.update_layout(
    title='Task Duration Over Runs (Interactive)',
    xaxis_title='Run Number',
    yaxis_title='Time (seconds)',
    hovermode='closest',  # Change hovermode to 'closest'
    template='plotly_dark',
    legend_title_text='Tasks'
)

# Show the plot
fig.show()

# Optional: Export the graph to an HTML file for sharing or viewing in a browser
fig.write_html("/home/sony/comp-project/interactive_visualization.html", include_plotlyjs='cdn')

