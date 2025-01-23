import json
import pandas as pd
from datetime import datetime, timedelta

class GHOrg:
    df = pd.DataFrame()
    def __init__(self, gh):
        super().__init__()
        self.gh = gh
    
    def from_gh (self):
        self.df = pd.DataFrame(self.gh.get_organizations())
        self.org_columns = self.df.columns

    def fetch_repos(self):
        self.df['repositories'] = self.df.apply(lambda x: self.gh.get_org_repos (x.repos_url), axis=1)

    def fetch_repo_details(self):
        self.df['repositories'].apply(self.repo_details)

    def repo_details(self, repoList):
        for item in repoList:
            result = self.gh.get_repo_info (item)
            item['repo_hooks'] = result[0]
            item['repo_branches'] = result[1]
            item['repo_pulls'] = result[2]
    
    def fetch_workflow_runs(self):
        self.df['repositories'].apply(self.workflow_runs)

    def workflow_runs (self, repoList):
        for item in repoList:
            item['repo_workflows'] = self.gh.get_workflow_runs (item)

    def assign_team_to_repo (self, owner, team, permission):
        filtered_df = self.df.query(f"login == '{owner}'")
        team_url = ""
        for index, value in filtered_df['teams'].items():
            for item in value:
                if team == item ['name']:
                    team_url = item ['repositories_url']
                    break
        filtered_df['repositories'].apply(self.put_team_repo, args=(team_url,permission))
    
    def put_team_repo (self, repoList, team_url, permission):
         for item in repoList:
            print (self.gh.put_team_repo (team_url,item['full_name'],permission))
    
    def get_org_teams(self):
        self.df['teams'] = self.df.apply(lambda x: self.gh.get_org_teams (x.login), axis=1)


        
    

    

