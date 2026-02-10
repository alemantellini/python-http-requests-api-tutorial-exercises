# EJERCICIO 9 - List of blog titles
import requests
def get_titles():
    # Your code here
    titles = []
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    if response.status_code == 200:
        body = response.json()
        for post in body["posts"]:
            title = post["title"]
            if title:
                titles.append(title)
    else:
        print("Something went wrong")
    return titles
print(get_titles())
