from datetime import datetime
import time
import sys
from Trip import Trip
import Trip.CrudTrip as crud
import googlemaps
import pprint
import json

def main():
    with open('API_KEY','r') as f:
        API_KEY = f.readline()
    gmaps = googlemaps.Client(key = API_KEY)
    params = {'query':'tourist+spots+in+Taitung', 'key':API_KEY}
    result = gmaps._request('/maps/api/place/textsearch/json', params)
    print(json.dumps(result))
    

if __name__ == "__main__":
    main()
