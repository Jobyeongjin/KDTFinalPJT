import requests
import json

api_key = ""
queryType = "&QueryType=" + "ItemNewAll"
maxResults = "&MaxResults=" + "100"
start = "&start=" + "1"
searchTarget = "&SearchTarget=" + "Book"
output = "&output=" + "js"
version = "&Version=" + "20131101"


def search():
    URL = (
        "http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey="
        + api_key
        + queryType
        + maxResults
        + start
        + searchTarget
        + output
        + version
    )

    response = requests.get(URL)
    response_json = json.loads(response.text)
    print(len(response_json["item"]))

    title_list = []
    for i in range(len(response_json["item"])):
        temp = response_json["item"][i]["title"]
        title_list.append(temp)

    print(title_list)


search()