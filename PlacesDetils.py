import googlemaps
import json
import csv
import pprint as pp
import requests

apik='Your API Key'

map_client=googlemaps.Client(apik)
#pp(response)
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

#for Taking the input
query = input("Enter the search")


r = requests.get(url + 'query=' + query +
                 '&key=' + apik)
x = r.json()
y = x['results']

#to Print the names of the places
for i in range(len(y)):
    print(y[i]['name'])

#to dump all the data into a json file
with open('FoodTruck json',"w") as f:
    json.dump(y,f,indent=2)
