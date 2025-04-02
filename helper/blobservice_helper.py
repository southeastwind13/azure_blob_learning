from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

import xml.etree.ElementTree as ET
import requests
import io

class BlobServiceHelper():
    '''
    require to add to the requirements.txt 
    - azure-storage-blob
    '''

    def __init__(self, connection_string:str, container_name:str):

        # Initialize the BlobServiceClient
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def get_file_content(self, myblob_name:str):
        '''
        Parameters
        :myblob_name: The name of the blob (myblob.name)
        '''
        container, blob_name = myblob_name.split("/")

        blob_client = self.blob_service_client.get_blob_client(container=container, blob=blob_name)
        
        blob_data = blob_client.download_blob()
        file_content = blob_data.readall()
        
        return file_content
    
    def parse_xml_content(self, content):
        xml_content = content.decode("utf-8")

        # Parse the XML content
        root = ET.fromstring(xml_content)

        # Extract some XML data (example: print all tags)
        parsed_data = {child.tag: child.text for child in root}

        return parsed_data
    
    def create_new_file(self, filename:str, filecontent:str):

        # Upload content to the blob
        blob_client = self.container_client.get_blob_client(filename)
        blob_client.upload_blob(filecontent, overwrite=True)

    def upload_image_from_url(self, image_url:str, file_name:str):
        '''
        file_name: A file name with filetype in the string format.
        
        '''
        file = requests.get(image_url)

        if not file:
            return func.HttpResponse("No file uploaded", status_code=400)
        
        blob_client = self.container_client.get_blob_client(file_name)
        blob_client.upload_blob(io.BytesIO(file.content), overwrite=True)

    def delete_blob_file(self, container_name:str, filename:str):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, 
            blob=filename)
        
        blob_client.delete_blob()

