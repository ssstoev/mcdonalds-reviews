import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("state_city_sentiment.csv")

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div([
    dbc.Container([
        dbc.Row(
            dbc.Col(
                html.H1("Average Sentiment Score and Review Count by City"),
            )
        ),

        dbc.Row([
            dbc.Col(html.P("Select a State"), width=3),
            dbc.Col(html.P("Select a Value"), width=3)
        ], style={"padding-top": "20px"}),
    
   
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='state-dropdown',
                    options=[{'label': state, 'value': state} for state in df['state'].unique()],
                    value=df['state'].unique()[0],  # Set default value
                    clearable=False,
                ), width = 3
            ),

            dbc.Col(
                    dcc.Dropdown(   
                    id='value-dropdown',
                    options=[{'label': "Compound Sentiment Score", 'value': "compound_sentiment_mean"},
                             {'label': "Positive Sentiment Score", 'value': "positive_sentiment_mean"},
                             {'label': "Negative Sentiment Score", 'value': "negative_sentiment_mean"},
                             {'label': "AVG Review (Stars)", 'value': "rating (stars)_mean"}],
                    value="compound_sentiment_mean",  # Set default value
                    clearable=False,
                    ), width = 3
            )
    ]),

    # Dropdown for selecting the state
    
    dbc.Row(
        dbc.Col(
            dcc.Graph(id='city-rating-graph')
        )
    )
    # Graph to display
    ]) 
])



# Callback to update the graph based on the selected state
@app.callback(
    Output('city-rating-graph', 'figure'),
    Input('state-dropdown', 'value'),
     Input('value-dropdown', 'value')
)
def update_graph(selected_state, selected_value):

    # Filter the DataFrame for the selected state
    filtered_df = df[df['state'] == selected_state]

    # Get the label for the selected value
    value_label = {
        "compound_sentiment_mean": "Compound Sentiment",
        "positive_sentiment_mean": "Positive Sentiment",
        "negative_sentiment_mean": "Negative Sentiment",
        "rating (stars)_mean": "Average Review (Stars)"
    }
    
    label_text = value_label.get(selected_value, 'Unknown')

    # Create the scatter plot
    fig = px.scatter(
        filtered_df,
        x='rating_count_count',
        y=selected_value,
        size='rating_count_count',  # Bubble size based on the number of reviews
        hover_name='city',
        title=f'Restaurants in cities in {selected_state}',
        labels={selected_value: label_text, 'rating_count_count': 'Number of Reviews in City'},
        color='city'  # Different color per city
    )
    
    # Update the layout
    fig.update_layout(
        xaxis_title='Total Count of Reviews',
        yaxis_title=label_text,
        title=f'Cities in {selected_state}',
        showlegend=False
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)