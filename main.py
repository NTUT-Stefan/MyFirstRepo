from datetime import datetime
import time
import sys
from Trip import Trip
import Trip.CrudTrip as crud
import googlemaps
import json 


def main():
    # 這是textsearch
    # gmaps = googlemaps.Client(key = '*******')
    # params = {
    #         'query': 'restaurant in Taipei Xinyi',
    #         'key': '*******',
    #     }
    # url_part = 'text'
    # url = "/maps/api/place/%ssearch/json" % url_part
    # x = gmaps._request(url, params)
    # print(json.dumps(x))
    # f = open("places.txt", "a")
    # f.write(json.dumps(x))
    # f.close()

    # 這是nearby search

    gmaps = googlemaps.Client(key = '')
    params = {
            'location': '25.033018,121.562801',
            'radius':  '1000',
            'key': '',
            'keyword': 'food',
            'language': 'zh-TW'
        }
    url_part = 'nearby'
    url = "/maps/api/place/%ssearch/json" % url_part
    x = gmaps._request(url, params)
    print(json.dumps(x))
    f = open("places.txt", "a")
    f.write(json.dumps(x))
    f.close()

if __name__ == "__main__":
    main()
