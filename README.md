API Consumer Toolkit

This Python project provides a comprehensive collection of modules for interacting with various DevOps tools through their APIs. It simplifies communication with Jenkins, GitHub, SonarQube, Nexus, and other endpoints, allowing you to automate tasks and streamline your development workflow.

The toolkit is designed to standardize API interactions across multiple platforms while providing a consistent interface for common DevOps operations.
Features

    Unified API access to multiple DevOps tools

    Consistent error handling and authentication flows

    Pagination support for API endpoints that return large datasets

    Pandas DataFrame integration for easy data manipulation

    Reusable base classes to simplify extending functionality

Installation

To install the package, run the following command in your terminal:

text
pip install apiconsumer

Alternatively, you can install directly from the GitHub repository:

text
pip install git+https://github.com/pjesensk/api-consumer.git

Requirements

The package requires Python 3.7 or higher and depends on the following libraries:

    requests

    python-dotenv

    pandas

    numpy

    hvac

    jinja2

    cryptography

    wheel

Modules Overview

The API Consumer toolkit includes modules for interacting with the following services:
Confluence Module

Provides functionality to interact with Confluence API:

python
from apiconsumer.confluence import ConfluenceApi

# Initialize the API client
confluence = ConfluenceApi(hostname="https://your-confluence-instance.com", auth_token="your-token")

# Get all spaces
spaces = confluence.get_spaces()

# Update a page
confluence.update_page(page_id="123456", new_content="Updated content")

GitHub Module

Facilitates interaction with GitHub API for repositories, organizations, and more:

python
from apiconsumer.github import GHApi
from apiconsumer.github.organizations import GHOrg

# Initialize the GitHub API client
github = GHApi(hostname="github.com", github_token="your-token")

# Get organization repositories
org = GHOrg(github)
org.from_gh()
org.fetch_repos()

HashiCorp Vault Module

Manages secrets in HashiCorp Vault:

python
from apiconsumer.hvault import HVault

# Initialize the Vault client
vault = HVault(url="https://your-vault-instance.com", token="your-token")

# Read a secret
secret = vault.read_secret("path/to/secret")

# Create or update a secret
vault.create_or_update("path/to/secret", {"key": "value"})

IBM Cloud Module

Interacts with IBM Cloud services:

python
from apiconsumer.ibmcloud import IC

# Initialize the IBM Cloud client
ibmcloud = IC(url="https://cloud.ibm.com/api", 
              iam_url="https://iam.cloud.ibm.com/identity/token", 
              auth_token="your-apikey")

Jenkins Module

Provides access to Jenkins API for job management and build statistics:

python
from apiconsumer.jenkins import JenkinsApi

# Initialize the Jenkins client
jenkins = JenkinsApi(hostname="https://your-jenkins-instance.com", 
                     username="your-username", 
                     token="your-token")

# Execute a Groovy script
result = jenkins.post_script("path/to/script.groovy")

# Get build information
builds = jenkins.get_builds()

JFrog Module

Interacts with JFrog Artifactory:

python
from apiconsumer.jfrog import JFrogAPI

# Initialize the JFrog client
jfrog = JFrogAPI(hostname="https://your-jfrog-instance.com", 
                 username="your-username", 
                 token="your-token")

# Get all users
users = jfrog.get_all_users()

# Create a user
jfrog.create_user("username", "email@example.com", "password", ["group1", "group2"])

Kubernetes Module

Facilitates interaction with Kubernetes clusters:

python
from apiconsumer.kubernetes import Kapi

# Initialize the Kubernetes client
k8s = Kapi(cluster_url="https://your-k8s-cluster", token="your-token")

# List pods in a namespace
pods = k8s.list_pods(namespace="default")

# List all namespaces
namespaces = k8s.list_namespaces()

Nexus Module

Provides integration with Nexus Repository Manager:

python
from apiconsumer.nexus import NexusApi  # Module exists but implementation details not available

SBOM Module (Software Bill of Materials)

Interacts with Dependency Track for SBOM management:

python
from apiconsumer.sbom import DTrack

# Initialize the Dependency Track client
dtrack = DTrack(url="https://your-dtrack-instance.com", token="your-token")

# Paginate through results
dtrack.paging("https://your-dtrack-instance.com/api/v1/components")

SonarQube Module

Provides access to SonarQube API for code quality analysis:

python
from apiconsumer.sonar import Sonar

# Initialize the SonarQube client
sonar = Sonar(url="https://your-sonar-instance.com", token="your-token")

# Paginate through components
sonar.paging("https://your-sonar-instance.com/api/components/search", {"p": 1})

Sysdig Module

Interacts with Sysdig for container monitoring and security:

python
from apiconsumer.sysdig import SysDig

# Initialize the Sysdig client
sysdig = SysDig(url="https://your-sysdig-instance.com", token="your-token")

# Paginate through results
sysdig.paging("https://your-sysdig-instance.com/api/data")

Common Patterns

All API modules inherit from the APIParent class, which provides common functionality:

python
from apiconsumer.apiparent import APIParent

class CustomAPI(APIParent):
    def __init__(self, url, token):
        super().__init__()
        self.url = url
        self.session.headers = {"Authorization": f"Bearer {token}"}
        
    def get_resource(self, resource_id):
        response = self.session.get(f"{self.url}/resources/{resource_id}")
        return response.json() if response.status_code == 200 else None

Utility Functions

The toolkit includes utility functions for common operations:

python
from apiconsumer.utils import print_arr, print_dict, to_json, from_json

# Print all items in an array
print_arr(["item1", "item2", "item3"])

# Print all key-value pairs in a dictionary
print_dict({"key1": "value1", "key2": "value2"})

# Save a pandas DataFrame to a JSON file
to_json(dataframe, "output.json")

# Load a pandas DataFrame from a JSON file
dataframe = from_json("input.json")

Project Structure

The repository is organized as follows:

text
api-consumer/
├── .github/
│   └── workflows/
│       └── build-release.yaml
├── apiconsumer/
│   ├── __init__.py
│   ├── apiparent.py
│   ├── utils.py
│   ├── confluence/
│   ├── github/
│   ├── hvault/
│   ├── ibmcloud/
│   ├── jenkins/
│   ├── jfrog/
│   ├── kubernetes/
│   ├── nexus/
│   ├── sbom/
│   ├── sonar/
│   └── sysdig/
├── README.md
├── pyproject.toml
├── requirements.txt
└── setup.py

License

This project is licensed under the MIT License.
Author

    Pavol Jesensky (pjesensky@gmail.com)

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
