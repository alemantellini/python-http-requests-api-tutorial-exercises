# EJERCICIO 5 - Project name
import requests
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")
if response.status_code == 200:
    body = response.json()
    project_name = body["name"]
    print(project_name)
else:
    print("Something went wrong")
