# Foodier

This project was created by:
  * Levy Shi
  * Shally Guo
  * Jimmy Huang
  * Mark Estudodillo
# Inspiration
From personal experiences, there are times when I want to eat out, but don't really have an idea of where exactly I want to eat. From there, my next plan of action would be to scroll through Yelp's list of restaurants to find a new place to dine. However, even though Yelp's services does offer an abundance of wonderful recommendations, at the end of the search, I always get overwhelmed with the number of options, and then find myself dinning at the same four restaurants that I always go. So, to prevent this, and encourage other users (and myself) to step out of my comfort zone and try out new restaurants, this app was created in a way that gave the users images of food and, from the users' preferences, output a recommend list of local restaurants to dine in.

# What it does
This web application displays various images of cuisines to a user. After a set number of images displayed, the web application uses machine learning in order to "learn" which food dishes a user prefers. From there, the application returns a list of recommended restaurants suitable to the user.

# How I built it
The framework of our web application was built with HTML, CSS, and Javascript. Additionally, we used Yelp Fusion API to generate a dictionary of the images and restaurants based on user's preference on location and zip code. From there, we used machine learning with Amazon Web Services's Rekognition, to filter out the images from Yelp to just output those images that contain food items. Outputting these images to the user and using the user's input to those food items, our final web application generates a final list of recommended restaurants to the users.

# Challenges I ran into
A main challenge that we ran into is altering what we have such as an image file to be what we need for a method. For example for the AWS Rekognition calls, we needed S3 objects and we had to find a way to turn a web url into a S3 object that we could use. There was also issues with having the different languages we were working on communicate with each other, such as JavaScript and Python and making use of what we had obtained from one to the other.

# Accomplishments that I'm proud of
We thought of a pretty cool idea that would be fun to use to help people decide what they may be interested in eating when they are not sure. It is not as complete as we would want it to be but it definitely was enjoyable to work on.

# What I learned
We learned how to do web development better as well as the many useful API's that are available to us. We have become more comfortable with using the Yelp API as well as the AWS API calls.

# What's next for Foodier
We want to find a way to pass the image files from JavaScript to python and then determine if the dish they are viewing is what they want or not by using the facial recognition from AWS Rekognition to obtain the users mood when viewing the dish. We would have the camera on and obtain a temporary image of the user to use as the image file.
