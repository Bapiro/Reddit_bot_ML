import json


with open('data.json', encoding='utf-8') as f:
    data = json.load(f)


print("title: " + data[0]["postTitle"])
print("comment: " + data[0]["bestcomment"][2])
