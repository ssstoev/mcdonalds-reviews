'''In this file we create an interactive map which displays the stores across the US map
    and it includes a popup functionality to view info about the specific stores.'''


import pandas as pd
import folium 
from folium import plugins
import matplotlib
import matplotlib.pyplot as plt
import branca

data = pd.read_csv("McDonald_s_Reviews.csv", encoding='ISO-8859-1')
data.dropna(inplace=True)

# Convert the rating column to a numeric one
data.loc[:, "rating (stars)"] = data["rating"].str.split(' ').map(lambda x: x[0] if len(x) > 0 else None)
data = data.drop(["rating"], axis=1)
data["rating (stars)"] = data["rating (stars)"].astype(int)

m = folium.Map(location=[data["latitude "].mean(), data["longitude"].mean()], zoom_start=6)

nr_ratings_min, nr_ratings_max = data["rating_count"].min(), data["rating_count"].max()

# Normalize ratings_count and the given stars to use for color mapping
# norm_rating_count = plt.Normalize(data['rating_count'].min(), data['rating_count'].max())
norm_rating_stars = plt.Normalize(data["rating (stars)"].min(), data["rating (stars)"].max())

# Create a colormap
#cmap = plt.cm.get_cmap('RdYlGn')
cmap = plt.colormaps["RdYlGn"]

for _, row in data.iterrows():

    popup_info = f''''Rating for restaurant: {row["rating (stars)"]} <br>
    Number of ratings for restaurant: {row["rating_count"]}
    '''
    # Normalize the rating and map to a color
    # normalized_value = norm_rating_count(row['rating_count'])
    normalized_rating_stars = norm_rating_stars(row["rating (stars)"])
    color = cmap(normalized_rating_stars)
    
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

# Add a color scale (legend) from red to green
colormap = branca.colormap.LinearColormap(colors=['red', 'yellow', 'green'], vmin=0, vmax=5)
colormap.caption = "Rating (Stars)"
colormap.add_to(m)

plugins.MiniMap().add_to(m)

m.save("mc_donalds_interactive_map.html")