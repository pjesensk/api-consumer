import json
from apiparent import APIParent
import pandas as pd

class DTrack(APIParent):
    df = pd.DataFrame()
    def __init__(self, url, token):
        super().__init__()
        self.session.headers = {
            "Content-Type": "application/json",
            "X-Api-Key": token,
            "Accept": "application/json",
        }
        self.url = url

    def paging (self,url, offset=0, limit=1000):
        response = self.session.get(url, params={"offset": offset, "limit": limit })
        
        #response.raise_for_status()  
        if response.status_code == 200:
            result = pd.DataFrame(response.json())
            if not result.empty:
                if self.df.empty:
                    self.df = result
                else:
                    self.df.merge (result, on=['name','version'], how="left") 

            # Extract the URL for the next page from the Link header
            count_header = response.headers.get("X-Total-Count")
            if count_header and int(count_header) > (offset + 1) * limit:
                  self.paging(url, offset + 1, limit )                         
        else:
            print(f"Error fetching {url} with response code: {response.status_code}")
       
    def get_projects(self):
        return self.paging(f"{self.url}/api/v1/project") 

