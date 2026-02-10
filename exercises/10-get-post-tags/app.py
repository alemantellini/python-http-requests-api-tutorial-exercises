# EJERCICIO 10 - Get post tags
import requests
def get_post_tags(post_id):
    # Your code here
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    if response.status_code == 200:
        body = response.json()
        for post in body["posts"]:
            if post["id"] == post_id:
                return post["tags"]
    else:
        print("Something went wrong")
print(get_post_tags(146))
