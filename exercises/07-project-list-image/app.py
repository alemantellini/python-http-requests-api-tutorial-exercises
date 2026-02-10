# EJERCICIO 7 - Project List Image
import requests
response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
if response.status_code == 200:
    body = response.json()
    project_url = body[2]["images"][2]
    print(project_url)
else:
    print("Something went wrong")
