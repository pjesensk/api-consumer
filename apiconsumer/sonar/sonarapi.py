import json
from apiconsumer.apiparent import APIParent
import pandas as pd

class Sonar(APIParent):
    df = pd.DataFrame()
    def __init__(self, url, token):
        super().__init__()
        self.session.auth = token, ''
        self.url = url

    def paging (self,url, params):
        response = self.session.get(url, params=params)
        
        #response.raise_for_status()  
        if response.status_code == 200:
            result = pd.DataFrame(response.json()['components'])
            if not result.empty:
                if self.df.empty:
                    self.df = result
                else:
                    self.df.merge (result, on=['key','name','project'], how="left") 
            paging = response.json()['paging']
            # Extract the URL for the next page from the Link header
            print (f"Index: {paging['pageIndex']}, Total: {paging['total']}")
            if int(paging['pageIndex']) * int(paging['pageSize']) < int(paging['total']):
                params['p'] = int(paging['pageIndex']) + 1
                self.paging(url, params )                         
        else:
            print(f"Error fetching {url} with response code: {response.status_code}")
            print (response.json())
       
    def get_projects(self, params = {'qualifiers': 'TRK', 'p':1, 'ps':500}):
        return self.paging(f"{self.url}/api/components/search",params) 

    def get_projects_stats (self):
        self.df['stats'] = self.df.apply(lambda x: self.get_project_status (x.key), axis=1)

    def get_project_status(self, project_key):
        response = self.session.get(f"{self.url}/api/qualitygates/project_status", params = {'projectKey': project_key})
        
        #response.raise_for_status()  
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching {url} with response code: {response.status_code}")
