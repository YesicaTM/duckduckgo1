from pip._vendor import requests
from operator import itemgetter

url_ddg = "https://api.duckduckgo.com"

resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
rsp_data = resp.json()['RelatedTopics']

pres_list = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Van Buren", "Harrison", "Tyler",
                 "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield",
                 "Arthur", "Cleveland", "Mckinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover",
                 "Truman", "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama",
                 "Trump", "Biden"]
url_list = []
text_list = ""

for item in rsp_data:
    url_list.append(item)

for k in url_list:
        # print(k['Text'])
    text_list += (k['Text'])
counter = 0

print(text_list)


