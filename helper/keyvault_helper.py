from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class KeyVaultHelper():
    '''
    require to add to the requirements.txt
    - azure-identity
    - azure-keyvault-secrets
    '''
    def __init__(self, keyvault_url:str):
        self.keyvault_url = keyvault_url
        self.credential = DefaultAzureCredential()
        self.secret_client = SecretClient(
            vault_url=self.keyvault_url, 
            credential=self.credential)

    def get_secret_key(self, key_name:str):
        secret = self.secret_client.get_secret(key_name)
        return(secret.value)