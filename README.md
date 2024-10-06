# mcdonalds-reviews

An analysis on over 33k reviews of McDonald restaurants accross the US. It includes an interactive map of the stores where you can scroll to see them. Also it has a sentiment analysis of the text reviews.

We created a map of the restaurants accross the US and the color coding shows the reviews at each restaurant.
![image](https://github.com/user-attachments/assets/cf6ec060-fae0-457f-a378-2ba72b034990)


There is also an interactive dashboard where you can choose to observe different metrics like avg rating in stars or sentiment score given to McDonald restaurants in different citites. There is also a filter for state.

![image](https://github.com/user-attachments/assets/886a400f-e909-4728-96e1-bc67498a0793)

The sentiment analysis is performed using the Vader library in python. Some additional words were added to increase sentiment, e.g. "spit", "cold", "tasteless", etc.
Using the dashboard one can focus on cities with low ratings and see what were the main issues there.
