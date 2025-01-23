import requests
import json
import re
import pandas as pd
from apiparent import APIParent

class IC(APIParent):
    api_limit=100
    api_first=1
    api_version="2024-10-15"
    api_generation="2"
    access_token = ""
    df = pd.DataFrame()
    def __init__(self,url, iam_url, auth_token):
        super().__init__()
        self.hostname = url
        self.auth_token = auth_token
        #get bearer token
        self.session.headers = {'Content-Type': 'application/x-www-form-urlencoded','Accept': 'application/json'}
        response = self.session.post(f"{iam_url}", data={'grant_type':'urn:ibm:params:oauth:grant-type:apikey','apikey':auth_token}) 
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            self.session.headers = {'Authorization': f'Bearer {self.access_token}'}
        else:
            raise Exception(f"Error fetching bearer token: {response.status_code}")
        
    def paging (self,url, params, data_field, merge_key):
        response = self.session.get(url, params=params)
        #response.raise_for_status()  
        if response.status_code == 200:
            payload =  response.json()

            result = pd.DataFrame(payload[data_field])
            if not result.empty:
                if self.df.empty:
                    self.df = result
                else:
                    self.df.merge (result, on=merge_key, how="left") 
            if 'next' in payload and payload['next']:
                del params [first]
                self.paging(url, params, data_field, merge_key )          

        else:
            print(f"Error fetching {url} with response code: {response.status_code}")

    def get_vpcs (self, params= {"limit": api_limit, "first": api_first, "version": api_version, "generation": api_generation}):
        return self.paging(f"{self.hostname}/vpcs", params, "vpcs", "crn") 

    def get_instances (self, params= {"limit": api_limit, "first": api_first, "version": api_version, "generation": api_generation}):
        return self.paging(f"{self.hostname}/instances", params, "instances", "crn") 

    def get_clusters (self, params= {"limit": api_limit, "first": api_first, "version": api_version, "generation": api_generation}):
        results = []
        response = self.session.get(f"https://containers.cloud.ibm.com/global/v1/clusters")
        #response.raise_for_status()  
        if response.status_code == 200:
            for item in response.json():
                detail_response = self.session.get(f"https://containers.cloud.ibm.com/global/v1/clusters/{item['id']}")
                results.append (item | detail_response.json())
            return results
