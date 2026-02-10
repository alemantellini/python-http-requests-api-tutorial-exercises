# EJERCICIO 8 - Post blog author
import requests
response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
if response.status_code == 200:
    body = response.json()
    author = body["posts"][0]["author"]["name"]
    print(author)
else:
    print("Something went wrong")
