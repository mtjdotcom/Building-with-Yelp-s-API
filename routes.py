from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import requests
import rauth
import json



app = Flask(__name__)

app.config["DEBUG"] = True
app.config.from_object(__name__)

@app.route("/")
def main():
	params = {"term": "sushi", "location": "94114", "radius_filter": "2000"}
	#Obtain these from Yelp's manage access page
	

	session = rauth.OAuth1Session(
	consumer_key = consumer_key
	,consumer_secret = consumer_secret
	,access_token = token
	,access_token_secret = token_secret)
 
	request = session.get("http://api.yelp.com/v2/search",params=params)

#Transforms the JSON API response into a Python dictionary
	data = request.json()
	session.close()
	return render_template('main.html', data=data)

# start the development server using the run() method
if __name__== "__main__":
	app.run(debug=True)

# def get_search_parameters(lat,long):
#   #See the Yelp API for more details
#   params = {}
#   params["term"] = "sushi"
#   params["ll"] = "{},{}".format(str(lat),str(long))
#   params["radius_filter"] = "2000"
#   params["limit"] = "10"
 
#   return params

# @app.route("/test/<search_query>")
# def search(search_query):
# 	return search_query

# @app.route("/integer/<int:value>")
# def int_type(value):
# 	print value + 1
# 	return "correct!"

# @app.route("/float/<float:value>")
# def float_type(value):
# 	print value + 1
# 	return "correct!"

# @app.route("/path/<path:value>")
# def path_type(value):
# 	print value
# 	return "correct!"	

# @app.route("/name/<name>")
# def index(name):
# 	if name.lower() == "michael":
# 		return "Hello, {}".format(name), 200
# 	else:
# 		return "Not Found", 404	