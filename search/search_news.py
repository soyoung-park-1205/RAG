import os
import urllib.request
import urllib.parse
import ssl
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("NAVER_CLIENT_ID", "")
client_secret = os.getenv("NAVER_CLIENT_SECRET", "")

ssl._create_default_https_context = ssl._create_unverified_context


def get_search_context(keyword):
    if not keyword:
        return ""
    search_result = ""
    for url in ["https://openapi.naver.com/v1/search/news.json"]:
        response = get_naver_search_response(keyword, url)
        search_result += "\n".join(delete_html_tag(document["title"]) + delete_html_tag(document["description"])
                                   for document in response["items"])
    return search_result

def delete_html_tag(content):
    soup = BeautifulSoup(content, "lxml")
    return soup.get_text()


def get_naver_search_response(keyword, url):
    query = urllib.parse.quote(keyword)
    url = f"{url}?query={query}&display=10&start=1&sort=sim"
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
