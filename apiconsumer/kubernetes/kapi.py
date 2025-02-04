import requests
import json
import re
import pandas as pd
from apiconsumer.apiparent import APIParent
from kubernetes import client, config

class Kapi(APIParent):
    def __init__(self, cluster_url, token):
        super().__init__()
        configuration = client.Configuration()
        configuration.host = cluster_url
        configuration.api_key["authorization"] = "Bearer " + token
        configuration.ssl_ca_cert = None 
        configuration.verify_ssl = False 
        client.Configuration.set_default(configuration)
        self.api_client = client.ApiClient(configuration)
        self.core_v1_api = client.CoreV1Api(self.api_client)
        self.rbac_authorization_v1_api = client.RbacAuthorizationV1Api(self.api_client)


    def list_pods(self, namespace="default"):
        return self.core_v1_api.list_namespaced_pod(namespace=namespace)

    def list_namespaces(self):
        return self.core_v1_api.list_namespace()

    def read_namespaced_config_map(self, name, namespace):
        return self.core_v1_api.read_namespaced_config_map(name, namespace)

    def list_namespaced_config_maps(self, namespace):
        return self.core_v1_api.list_namespaced_config_map(namespace=namespace)

    def read_namespaced_pod(self, name, namespace):
        return self.core_v1_api.read_namespaced_pod(name, namespace)

    def create_namespaced_pod(self, body, namespace="default"):
        return self.core_v1_api.create_namespaced_pod(namespace=namespace, body=body)

    def delete_namespaced_pod(self, name, namespace="default"):
        return self.core_v1_api.delete_namespaced_pod(name, namespace=namespace)

    def create_namespaced_config_map(self, body, namespace="default"):
        return self.core_v1_api.create_namespaced_config_map(namespace=namespace, body=body)

    def delete_namespaced_config_map(self, name, namespace="default"):
        return self.core_v1_api.delete_namespaced_config_map(name, namespace=namespace)

    def create_namespace(self, body):
        return self.core_v1_api.create_namespace(body=body)

    def delete_namespace(self, name):
        return self.core_v1_api.delete_namespace(name=name)

    def create_cluster_role(self, body):
        return self.rbac_authorization_v1_api.create_cluster_role(body=body)

    def delete_cluster_role(self, name):
        return self.rbac_authorization_v1_api.delete_cluster_role(name=name)

    def create_cluster_role_binding(self, body):
        return self.rbac_authorization_v1_api.create_cluster_role_binding(body=body)

    def delete_cluster_role_binding(self, name):
        return self.rbac_authorization_v1_api.delete_cluster_role_binding(name=name)









