import requests
import json
import re
from apiconsumer.apiparent import APIParent

class JFrogAPI(APIParent):
    def __init__(self, hostname, username, token):
        super().__init__()
        self.hostname = hostname
        #self.session.auth = (username, token)
        #self.session.headers = {'Content-Type': 'application/json'}
        self.session.headers = {"Authorization": "Bearer " + token, "Accept": "application/json"}
        self.base_url = self.hostname 
        # load the current api spec
        print (self.get_all_users())

    def get_all_users(self):
        url = f"{self.base_url}/access/api/v2/users"
        response = self.session.get(url)
        return response.json()

    def create_user(self, username, email, password, groups=None):
        url = f"{self.base_url}/access/api/v2/users"
        data = {
            "username": username,
            "email": email,
            "password": password,
            "groups": groups if groups else []
        }
        return self.session.post(url, json=data).json()
