from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class KeyVaultHelper():
    '''
    1. require to add to the requirements.txt
    - azure-identity
    - azure-keyvault-secrets

    2. Enable identity of Azure function.
    3. Go to IAM of Keyvault and give permission to the Azure function.
    4. Get URL of Keyvalut by nevigate to overview of Keyvault page.
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