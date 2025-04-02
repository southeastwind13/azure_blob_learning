1. Install or update Core Tools
- Open command palette in VScode by press "F1" or command+shift+p
- Search for "Azure Functions: Install or Update Core Tools"

2. Create project on local
- Open command palette in VScode by press "F1" or command+shift+p
- Search for "Azure Functions: Create New Project...."

3. Deploy project
- Open command palette in VScode by press "F1" or command+shift+p
- Search for "Azure Functions: Deploy to Function App"
- You can chose to deploy to the existing resource or create a new one.

4. Add require library on the requirements.txt

Request pattern
- https://{app-name}.azurewebsites.net/api/{function-route}{?name=pong}

5. If you want to access another resources you can do
- Enable Azure function identity 
    - Navigate to Identity (Under Settings) → Enable System Assigned Managed Identity.
- Go to IAM on specific resource and give a permission.

6. Use custom module
- Set the path of the project
    - dir_path = os.path.dirname(os.path.realpath(__file__))
      sys.path.insert(0, dir_path)

7. Change authorize to be Authonomous
    - app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

8. Environment variable
- We can add environment variable under the value section in the local.settings.json