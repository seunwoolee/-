import requests
from bs4 import BeautifulSoup
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NAVER = 'https://news.naver.com/'
req = requests.get(NAVER)

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('#ranking_101 ul.section_list_ranking > li > a')
for post in posts:
    URL = NAVER+post.get('href')
    # print(URL)
    sub_req = requests.get(URL)
    # sub_req.select("main_content")
    sub_html = sub_req.text
    sub_soup = BeautifulSoup(sub_html, 'html.parser')
    print(sub_soup)
    # sub_post = sub_soup.select("#cbox_module")
    # print(sub_post)