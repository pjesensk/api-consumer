API Consumer Toolkit

This Python project provides a collection of modules for interacting with various DevOps tools through their APIs. It simplifies communication with Jenkins, GitHub, SonarQube, Nexus, and other endpoints.
Features

    Jenkins Module: Streamlines interactions with Jenkins APIs.
    GitHub Module: Provides tools to interact with GitHub repositories, issues, and workflows.
    SonarQube Module: Simplifies access to SonarQube's analysis data.
    Nexus Module: Facilitates communication with Nexus repositories.

Installation

To install the package, run the following command in your terminal:
bash

pip install api_consumer

Usage

The project consists of several modules, each dedicated to a specific API. Here's a basic overview of their functionalities:
Jenkins Module

    Automate builds and deployments.
    Fetch build details and logs.

GitHub Module

    Manage repositories and issues.
    Trigger workflows and analyze pull requests.

SonarQube Module

    Retrieve code quality metrics.
    Manage projects and issues.

Nexus Module

    Manage artifacts and dependencies.
    Query repository statistics.

Repository Details

    Owner: pjesensk
    Default Branch: main
    Languages: Python (98.1%), Groovy (1.9%)
    License: MIT License (planned but not explicitly stated in the repository)
    Visibility: Public
    Topics: (No topics have been added yet)

Example Usage (Illustrative)

Here is a simple example of interacting with the GitHub module:
Python

from api_consumer.github_module import GitHubClient

client = GitHubClient(token="your_token")
repo_info = client.get_repository("pjesensk", "api-consumer")
print(repo_info)

Ongoing Work

    An open pull request titled "Update README.md" is currently being worked on.
    The repository has 1 open issue.

Contribution Guidelines

Contributions are welcome! Please follow these steps:

    Fork the repository.
    Create a new branch for your changes.
    Submit a pull request detailing your modifications.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Additional Information

    Created On: September 30, 2024
    Last Pushed: April 29, 2025
    Watchers: 0
    Forks: 0
