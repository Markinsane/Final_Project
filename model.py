import requests
import json
import secrets as secrets
from bs4 import BeautifulSoup
import sample_dic as sample
import sqlite3 as sqlite


# Author: Guanchao Huang 



# This is the class for store, it's input is name, rating and review, and it will print out a string.

class Store(object):

	def __init__(self, name, rating, review):
		self.name = name
		self.rating = rating
		self.review = review
	
	def __str__(self):
		return "{}, Rating:{}, Review:{} ".format(self.name, self.rating, self.review)


# This is the caching for yelp data

CACHE_FNAME = 'cache_file.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()


except:
    CACHE_DICTION = {}

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)


# This is to make query to Yelp and cache the data

def get_nearby_places_for_site(name="Los Angeles",term="bars",limit=25):

		headers = {'Authorization': 'Bearer %s' % secrets.api_key}
		baseurl = "https://api.yelp.com/v3/businesses/search"
		params_diction = {}
		params_diction["term"]=term
		params_diction["location"]=name
		params_diction["limit"]=limit
		unique_ident = params_unique_combination(baseurl,params_diction)
		if unique_ident in CACHE_DICTION:
			print("Getting cached data...")

			return CACHE_DICTION[unique_ident] 
	    
	        
		else:    
			print("Making a request for new data...")
			resp = requests.get(baseurl, params=params_diction, headers=headers)
			CACHE_DICTION[unique_ident] = json.loads(resp.text)
			dumped_json_cache = json.dumps(CACHE_DICTION)
			fw = open(CACHE_FNAME,"w")
			fw.write(dumped_json_cache)
			fw.close()
			return CACHE_DICTION[unique_ident] 

# This is to aggregate all the information from yelp in a list that is comprised of many dictionaries.

def get_data_for_web(name="Los Angeles", term="bars"):
	ab=get_nearby_places_for_site(name, term)
	lst=[]
	for i in ab["businesses"]:
		info_lst=[]
		info_lst.append(i["name"])
		info_lst.append(i["rating"])

		if len(i["location"])==1:
			info_lst.append(i["location"]['display_address'][0])			
		else:
			info_lst.append(i["location"]['display_address'][0]+", "+i["location"]['display_address'][1])

		info_lst.append(i["image_url"])
		info_lst.append(i["url"])
		info_lst.append(i["review_count"])
		info_lst.append(i["display_phone"])
		info_lst.append(i["categories"][0]["title"])
		lst.append(info_lst)
	return lst



# This is the caching for for all the web scrawling and scraping for the site ENCYCLOPÆDIA BRITANNICA 

CACHE_FNAME = 'directory_dict.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()


except:
    CACHE_DICTION = {}


def get_unique_key(url):
  return url 


def make_request_using_cache(url):
    unique_ident = get_unique_key(url)


    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]

    else:
        print("Making a request for new data...")
        header = {'User-Agent': 'SI_CLASS'}
        resp = requests.get(url)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()

# This is to get the url for all the city on the ENCYCLOPÆDIA BRITANNICA website

def web_crawler():
	city_dic={}
	baseurl = 'https://www.britannica.com/topic/list-of-cities-and-towns-in-the-United-States-2023068'
	page_text = make_request_using_cache(baseurl)
	page_soup = BeautifulSoup(page_text, 'html.parser')
	content_div = page_soup.find(class_='content')
	link_div = content_div.find_all("a")
	for i in link_div:
		city_dic[i.text]=i["href"]
		url=i["href"]
	return city_dic


#This  is to create data base for city info.

def create_city_db():
    try:
        conn = sqlite.connect('city_info.sqlite')
        cur = conn.cursor()
    except Error as e:
        print(e)

    statement = '''
        DROP TABLE IF EXISTS 'Cities';
    '''
    cur.execute(statement)

    create_table_statement = """
        CREATE TABLE 'Cities' (
      'Id' INTEGER PRIMARY KEY AUTOINCREMENT,  
      'Cities' TEXT NOT NULL, 
      'Info' TEXT NOT NULL 
    ); """
    print(create_table_statement)
    cur.execute(create_table_statement)
    conn.commit()



 # This is to crawl and scrape each url got from web_crawler() and then insert into database

def populate_city_db():

	conn = sqlite.connect('city_info.sqlite')
	cur = conn.cursor()
	for i in sample.sample_dict:
		url=sample.sample_dict[i]
		page_text = make_request_using_cache(url)
		if page_text !=None:
			page_soup = BeautifulSoup(page_text, 'html.parser')
			content_div = page_soup.find(class_='content')

			values=(None, i, content_div.text)
			another_statement="INSERT INTO Cities "
			another_statement+='VALUES (?, ?, ?)'
			cur.execute(another_statement,values)
		else:
			pass


		
	conn.commit()


 # This is to get information from database whenever user makes a request

def get_from_db(query="Los Angeles"):
	conn = sqlite.connect('city_info.sqlite')
	cur = conn.cursor()
	statement="""
	SELECT info, field3 
	FROM Cities 
	JOIN Top5000Population
	WHERE Cities = ? AND field1= ?
	"""

	params_1= (query, query)

	city_info=cur.execute(statement, params_1)
	lst=[]
	for i in city_info:
		lst.append(i[0][:550])
		lst.append(i[1])
	return lst



# This is is to scrape data from Mitsuku whenever user makes a request


def get_from_mitsuku(query="How are you?"):
	lst=[]
	data = {"message":query}
	r = requests.post("https://kakko.pandorabots.com/pandora/talk?botid=87437a824e345a0d&skin=mobile", data=data)
	page_text=r.text
	page_soup = BeautifulSoup(page_text, 'html.parser')
	content_div = page_soup.find_all('font')
	text_message=content_div[1]
	ab=text_message.text
	query=query.decode("UTF-8")
	lst.append(query)
	new="You: "+query.strip()+" Mitsuku:"
	mitsuku=ab.replace(new, "")
	lst.append(mitsuku)
	return lst






