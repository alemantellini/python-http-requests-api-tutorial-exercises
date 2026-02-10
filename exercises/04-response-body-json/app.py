# EJERCICIO 4 - Response JSON
import requests
response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
if response.status_code == 200:
    time = response.json()
    hours = time["hours"]
    minutes = time["minutes"]
    seconds = time["seconds"]
    print(f"Current time: {hours} hrs {minutes} min and {seconds} sec")
else:
    print("Something went wrong")
