'''In this file we create an interactive map which displays the stores across the US map
    and it includes a popup functionality to view info about the specific stores.'''


import pandas as pd
import folium 
from folium import plugins
import matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv("McDonald_s_Reviews.csv", encoding='ISO-8859-1')
data.dropna(inplace=True)
m = folium.Map(location=[data["latitude "].mean(), data["longitude"].mean()], zoom_start=6)

nr_ratings_min, nr_ratings_max = data["rating_count"].min(), data["rating_count"].max()

# Normalize ratings_count to use for color mapping
norm = plt.Normalize(data['rating_count'].min(), data['rating_count'].max())
# Create a colormap
cmap = plt.cm.get_cmap('RdYlGn')

for _, row in data.iterrows():

    popup_info = f''''Rating for store {row["rating"]} <br>
    Number of ratings for store: {row["rating_count"]}
    '''
    # Normalize the rating and map to a color
    normalized_value = norm(row['rating_count'])
    color = cmap(normalized_value)
    
    # Convert the RGBA color to hex for folium
    hex_color = matplotlib.colors.rgb2hex(color)

    folium.CircleMarker(
        location=[row["latitude "], row["longitude"]],
        radius=10,
        color=hex_color,
        fill=True,
        fill_Color=hex_color,
        fill_opacity=0.7,
        popup=folium.Popup(popup_info, max_width=300)
    ).add_to(m)

plugins.MiniMap().add_to(m)

m.save("mcdonalds_review.html")