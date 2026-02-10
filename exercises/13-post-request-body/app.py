# EJERCICIO 13 - POST request body
import requests
url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"
myobj = {
    "id": 2323,
    "title": "Very big project"
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, json = myobj, headers = headers)
print(response.text)
