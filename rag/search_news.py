import urllib.request
import urllib.parse
import ssl
import json

client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"

ssl._create_default_https_context = ssl._create_unverified_context


def get_search_context(keyword):
    response = get_news_search_response(keyword)
    items = response["items"]
    context = ""
    for document in items:
        context += document["description"] + "\n"
    return context


def get_news_search_response(keyword):
    query = urllib.parse.quote(keyword)
    url = f"https://openapi.naver.com/v1/search/news.json?query={query}&display=10&start=1&sort=sim"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    with urllib.request.urlopen(request) as response:
        code = response.getcode()
        if code == 200:
            response_body = response.read()
            return json.loads(response_body.decode('utf-8'))
        else:
            print("Response code:", code)
            return None
