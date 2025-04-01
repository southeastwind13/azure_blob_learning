import azure.functions as func
import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helper')))

from helper.keyvault_helper import KeyVaultHelper

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
KEYVAULT_URL = "https://kv-func-demo-dev-fc.vault.azure.net/"

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    keyvault_helper = KeyVaultHelper(KEYVAULT_URL)
    keyname = "mykey"
    key = keyvault_helper.get_secret_key(keyname)
    

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"with {key}: Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"with {key}: This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )