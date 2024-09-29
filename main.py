import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("pivoted_data.csv")

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Average Rating and Review Count by City"),
    
    # Dropdown for selecting the state
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in df['state'].unique()],
        value=df['state'].unique()[0],  # Set default value
        clearable=False,
        style={'width': '50%'}
    ),
    
    # Graph to display
    dcc.Graph(id='city-rating-graph')
])

# Callback to update the graph based on the selected state
@app.callback(
    Output('city-rating-graph', 'figure'),
    [Input('state-dropdown', 'value')]
)
def update_graph(selected_state):
    # Filter the DataFrame for the selected state
    filtered_df = df[df['state'] == selected_state]
    
    # Create the scatter plot
    fig = px.scatter(
        filtered_df,
        x='rating (stars)',
        y='rating_count',
        size='rating_count',  # Bubble size based on the number of reviews
        hover_name='city',
        title=f'Cities in {selected_state}',
        labels={'rating (stars)': 'Average Rating (Stars)', 'rating_count': 'Average Count of Reviews'},
        color='city'  # Different color per city
    )
    
    # Update the layout
    fig.update_layout(
        xaxis_title='Average Rating (Stars)',
        yaxis_title='Average Count of Reviews',
        title=f'Cities in {selected_state}',
        showlegend=False
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)