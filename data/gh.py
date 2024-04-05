import requests
import urllib.parse
import json
import csv

url = "https://api.github.com/search/repositories"
query = urllib.parse.quote("iot", safe='/', encoding=None, errors=None)
head = {
    "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"
}

res = requests.get(url + "?q=" + query, headers=head)

# fields=['Project name', 'Tags','Description']

# print()
d = res.json()['items']
keys = res.json()['items'][0].keys()

with open('data1.csv', 'a', newline='', encoding='UTF-8') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(d)



# for item in res.json()['items']:
#     print("Repo Name: ",item['name'])
#     print("Topics: ", item['topics'])
#     print("description: \n", item['description'])
