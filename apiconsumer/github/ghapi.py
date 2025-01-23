import requests
import json
import re
from apiparent import APIParent

class GHApi(APIParent):
    def __init__(self, hostname, github_token):
        super().__init__()
        self.hostname = hostname
        self.github_token = github_token
        self.session.headers = {"Authorization": "Bearer " + self.github_token, "Accept": "application/json"}
        self.base_url = 'https://' + self.hostname 
        # load the current api spec
        self.api_dict = self.get_api_spec()

    def get_api_spec(self):
        response = self.session.get(f"{self.base_url}/api/v3") 
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching api spec: {response.status_code}")

    def gh_paging (self,url, per_page=100):
        response = self.session.get(url, params={"per_page": per_page})
        #response.raise_for_status()  
        if response.status_code == 200:
            return response.json()

            # Extract the URL for the next page from the Link header
            link_header = response.headers.get("Link")
            if link_header:
                next_url_match = re.search(r'<([^>]+)>; rel="next"', link_header)
                if next_url_match:
                    self.gh_paging(next_url_match.group(1),per_page)
        else:
            print(f"Error fetching {url} with response code: {response.status_code}")

    def get_organizations(self):
        return self.gh_paging(f"{self.base_url}/api/v3/organizations") 

    def get_org_teams(self, org):
        return self.gh_paging(f"{self.base_url}/api/v3/orgs/{org}/teams") 
    
    def get_org_repos(self,repos_url):
        return self.gh_paging(repos_url) 
     
    def get_repo_info(self, repo):
        pattern = r"{(.*?)}"
        hooksObj = self.gh_paging(re.sub(pattern, "", repo['hooks_url']))
        branchesObj = self.gh_paging(re.sub(pattern, "", repo['branches_url']))
        pullsObj = self.gh_paging(re.sub(pattern, "", repo['pulls_url']))
        return (hooksObj,branchesObj,pullsObj)
    
    def get_workflow_runs (self,repo):
        result = self.gh_paging(repo['url']+'/actions/runs')
        if result is not None:
            return result['workflow_runs']
        else:
            return []
    
    def put_team_repo (self,team_url,repo,params):
        print (f"{team_url}/{repo}")
        return self.session.put(f"{team_url}/{repo}",params=params )

