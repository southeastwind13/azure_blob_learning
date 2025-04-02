import azure.functions as func
import logging
import os
import sys

# dir_path = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, dir_path)

# from helper.keyvault_helper import KeyVaultHelper

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
# KEYVAULT_URL = "https://kv-funcdemo-dev-fc.vault.azure.net/"

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    logging.info('Python HTTP trigger function processed a request.')

    # keyvault_helper = KeyVaultHelper(KEYVAULT_URL)
    # keyname = "mykey"
    # key = keyvault_helper.get_secret_key(keyname)
    
    return func.HttpResponse(f"this is my key:")