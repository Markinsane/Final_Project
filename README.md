Name : Magic City 
Author: Guanchao Huang 




- App Overview

This web application allows user to explore a new city with ease, I listed some of the key features here.

1. Search for various kinds of recreationl places in different cities.
2. Get to know each city's history and general information
3. Interact with the chatbot to carry on casual conversations.


- Data Source Used 

1. Yelp API for information about different places in a city 
2. ENCYCLOPÆDIA BRITANNICA (https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068)
  to get history and general information about a city. (multiple page scraping and crawling)
3. Mitsuku Online chatbot (https://kakko.pandorabots.com/pandora/talk?botid=87437a824e345a0d&skin=mobile)

- Data Storage 

1. All Yelp Api data are stored in a cache file named cache_file
2. City information are first crawled and scraped while caching and then put into a database called city_info.sqlite, which contains two tables. 


- Code Structure.

* Model: model.py
1. get_nearby_places_for_site() is used to make query to Yelp and cache the data
2. get_data_for_web() is to aggregate all the information in a list that is comprosed of many dictionaries.
3. web_crawler() is used to get the url for all the city on the ENCYCLOPÆDIA BRITANNICA website
4. create_city_db() is to create data base. 
5. populate_city_db() is to crawl and scrape each url got from web_crawler() and then insert into database
6. get_from_db is to get information from database whenever user makes a request
7. get_from_mitsuku() is to scrape data from Mitsuku whenever user makes a request

* View: Project2.html
1. it's a html file that renders the page, all the dependencies (css, javascript, images) are listed in the static foler 

* Controller: app.py
1. @app.route('/', methods=['GET', 'POST']) handle routing when use make either a get or post request
2. @app.route('/process', methods=['POST']) is to handle all the AJAX call from client side (javascript from client side, and information would be updated without refreshing the page)



- Instruction for running the app

1. Install all the dependencies in the requirement.txt
2. Get a yelp fusion api key and put it the secrets.py file 
3. Run the app.py file in the termial, you will get a link to your local host (http://127.0.0.1:5000/), go to your local host and you can start interacting with the app


- FYI

I already hosted the web application on Heroku, so if you want to check it out, the url is https://magic-city.herokuapp.com


HAVE FUN USING THE APP !!!! 





