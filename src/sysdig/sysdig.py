import json
import pandas as pd
from apiparent import APIParent

class SysDig(APIParent):
    df = pd.DataFrame()
    def __init__(self, url, token):
        super().__init__()
        self.url = url
        self.token = token
        self.session.headers = {"Authorization": "Bearer " + self.token, "Accept": "application/json"}

    def paging (self,url, params={'limit': 1000}):
        response = self.session.get(url, params=params)
        
        #response.raise_for_status()  
        if response.status_code == 200:
            result = pd.DataFrame(response.json()['data'])
            if not result.empty:
                if self.df.empty:
                    self.df = result
                else:
                    self.df.merge (result, on=['resultId'], how="left") 

            # Extract the URL for the next page from the Link header
            if 'next' in response.json()['page']:
                  self.paging(url, {'limit': params['limit'], 'cursor': response.json()['page']['next']} )                         
        else:
            print(f"Error fetching {url} with response code: {response.status_code}")

    def get_vulnerabilities(self):
        return self.paging(f"{self.url}/secure/vulnerability/v1beta1/pipeline-results")
        