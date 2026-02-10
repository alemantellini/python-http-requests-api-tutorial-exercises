# EJERCICIO 6 - Project list
import requests
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
if response.status_code == 200:
    body = response.json()
    project_name = body[1]["name"]
    print(project_name)
else:
    print("Something went wrong")
