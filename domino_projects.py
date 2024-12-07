#!/usr/bin/env python

import os
import requests
import logging

DOMINO_API_KEY = os.getenv("DOMINO_API_KEY")
DOMINO_URL = "https://prod-field.cs.domino.tech/v4/projects"

logging.basicConfig(
    filename = "log.log",
    level = logging.DEBUG

)
# Define the request headers
headers = {
    "accept": "application/json",
    "X-Domino-Api-Key": DOMINO_API_KEY
}

def query_api():
    # Send request to the API
    logging.info(f"Calling the API {DOMINO_URL}")
    print(f"Calling the API {DOMINO_URL}")
    try:
        response = requests.get(DOMINO_URL, headers=headers)
        if response.status_code == 200:
            return response.json()

    except:
        logging.Error(f"Calling the API{DOMINO_URL} Failed")    
        print(f"Calling the API{DOMINO_URL} Failed")    

def process_projects(projects):
    # process the data
    for project in projects:
        print(project)
        print("\n") 
        for k,v in project.items():
            print(f"{k} : {v}")

def main():
    projects = query_api()
    if projects != None:
        process_projects(projects)


if __name__ == "__main__":
    main()