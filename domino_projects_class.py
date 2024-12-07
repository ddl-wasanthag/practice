#!/usr/bin/env python

import os
import requests
import logging


logging.basicConfig(
    filename = "log.log",
    level = logging.DEBUG

)

class Domino_Projects:
    def __init__(self, api_key, url):
        self.DOMINO_API_KEY = api_key
        self.DOMINO_URL = url

    def query_api():
        # Define the request headers
        headers = {
            "accept": "application/json",
            "X-Domino-Api-Key": DOMINO_API_KEY
        }

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


prod_field = Domino_Projects(os.getenv("DOMINO_API_KEY"), "https://prod-field.cs.domino.tech/v4/projects")
prod_field.main()