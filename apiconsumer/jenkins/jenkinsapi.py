import requests
import json
import re
import pandas as pd
from apiconsumer.apiparent import APIParent

class JenkinsApi(APIParent):
    df = pd.DataFrame()
    def __init__(self, hostname, username, token):
        super().__init__()
        self.hostname = hostname
        self.token = token
        self.username = username
        self.session.auth = (self.username, self.token)
        self.auth = self.session.post(self.hostname)
        self.get_builds()

    def post_script (self, script_file):
        with open(script_file, 'r') as file:
            response = self.session.post(f"{self.hostname}/scriptText", data={"script": file.read()})
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                print(f"Error executing script with response code: {response.status_code}")

    def get_builds (self):
        results = self.post_script("src/jenkins/jenkins_stats.groovy")
        self.df = pd.DataFrame(results)