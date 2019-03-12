from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NAVER = 'https://news.naver.com/'
timeout = 10
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(5)

driver.get(NAVER)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

for i in range(101,104):
    posts = soup.select('#ranking_{} ul.section_list_ranking > li > a'.format(i))

    for post in posts:
        URL = NAVER+post.get('href')
        driver.get(URL)
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(('className', 'u_cbox_contents'))
        )
        sub_html = driver.page_source
        sub_soup = BeautifulSoup(sub_html, 'html.parser')
        title = sub_soup.select("#articleTitle")
        reply = sub_soup.select("span.u_cbox_contents")
        writer = sub_soup.select("span.u_cbox_nick")
        up = sub_soup.select("em.u_cbox_cnt_recomm")
        down = sub_soup.select("em.u_cbox_cnt_unrecomm")
        print(up, down)