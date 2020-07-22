from datetime import datetime
import time
import sys
from Trip import Trip
import Trip.CrudTrip as crud



def main():
    with open('API_KEY','r') as f:
        API_KEY = f.readline()
    print(API_KEY)

if __name__ == "__main__":
    main()
