# EJERCICIO 11 - Get attachment by id
import requests
def get_attachment_by_id(attachment_id):
    # Your code here
    response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
    if response.status_code == 200:
        body = response.json()
        for post in body["posts"]:
            if "attachments" in post:
                for attachment in post["attachments"]:
                    if attachment["id"] == attachment_id:
                        return attachment["title"]
    else:
        print("Something went wrong")
print(get_attachment_by_id(137))
