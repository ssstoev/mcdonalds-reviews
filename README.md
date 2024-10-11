# mcdonalds-reviews
![image](https://github.com/user-attachments/assets/497cd77a-2fd6-44ec-92ad-72efe7f753a9)

An analysis on over 33k reviews for 40 McDonald's restaurants accross the US. It includes an interactive map of the stores where you can scroll to see them. The top mentioned words for each restaurant can appear like in the wordcloud above this text.  
We looked at the restaurants which people from highest to lowest and investigated what were the reasons for their reviews. By applying sentiment analysis tehcniques we listed the top complaints accross some of the restaurants.

We created a map of the restaurants accross the US and the color coding shows the average rating at each restaurant. The map is made using folium.
![image](https://github.com/user-attachments/assets/b6728fbe-c247-492e-a492-a46b41b47f52)

There is also an interactive dashboard where you can pick different states and observe metrics for the citites in the chosen state like avg rating in stars or sentiment score given to McDonald restaurants.

![image](https://github.com/user-attachments/assets/886a400f-e909-4728-96e1-bc67498a0793)

The sentiment analysis is performed using the Vader library in python. Some additional words were added to increase sentiment, e.g. "spit", "cold", "tasteless", etc.
