import googlemaps
import json
import csv
import requests

# a function to store the results into a JSON file
def storeIntoJson(results):
    #to dump all the data into a json file
    with open('FoodTruck json',"w") as f:
        json.dump(results,f,indent=4)

# Function to get the request from the API using the URL and the return a JSON file
def findPlaces(nurl):
    # the we will pass use a get request to get the data
    print("The requested URL = ", nurl)
    req = requests.get(nurl)

    # convert the request into JSON object
    x = req.json()
    return x


# a function to get next page
def getNextPage(nurl, x):
    nextPageToken=x['next_page_token']

    nurl=nurl+"pageToken="+nextPageToken
    print("The requested URL 2 = ",nurl)

    req=requests.get(nurl)
    x2=req.json()
    return x2


if __name__=='__main__':

    #The API Key
    #apik=input("Enter your API Key")

    apik='AIzaSyBqS_5RBg_KE5zV3QXQV5e9R1ytkUt3G1Q&'
    #Making the map client to pass in the Query
    #map_client=googlemaps.Client(apik)

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    #for Taking the input
    #query = input("Enter the search")
    #query='Foods+Truck+In+New+York'
    query="Coffee+shop+in+Tucson"
    # the response URL will be the URL+query='Query'&key=APIKey
    nurl=url + 'query=' + query +'&key=' + apik
    x=findPlaces(nurl)

    # the get json will pass a while lot of information such as next token and all but we only care about the results for now
    results = x['results']

    #to Print the names of the places
    #for i in range(len(results)):
    #    print(results[i]['name'])

    print(x,'\n\n',results)
    #to get the next page using the next page token
    nurl2=url + 'query=' + query +'&key=' + apik

    x2=getNextPage(nurl2,x)
    print(x2,"\n",x2['results'])
    # storing the results into a JSON file
    #storeIntoJson(results)
