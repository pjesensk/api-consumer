import hvac

class HVault:

    def __init__(self, url, token):
        super().__init__()
        self.client = hvac.Client(
            url=url,
            token=token,
        )

    def create_or_update (self, path, data):
        return self.client.secrets.kv.v2.create_or_update_secret(
            path=path,
            secret=data,
        )


    def read_secret (self,path):
        return self.client.secrets.kv.read_secret_version(path=path)