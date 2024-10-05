import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("state_city_sentiment.csv")

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Average Sentiment Score and Review Count by City"),
    
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
        x='sentiment_score_mean',
        y='rating_count_sum',
        size='rating_count_sum',  # Bubble size based on the number of reviews
        hover_name='city',
        title=f'Cities in {selected_state}',
        labels={'sentiment_score_mean': 'Average Sentiment Score', 'rating_count_sum': 'Total Count of Reviews in City'},
        color='city'  # Different color per city
    )
    
    # Update the layout
    fig.update_layout(
        xaxis_title='Average Sentiment Score',
        yaxis_title='Average Count of Reviews',
        title=f'Cities in {selected_state}',
        showlegend=False
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)