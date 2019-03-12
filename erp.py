from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

NAVER = 'http://kcerp4:81/jde/E1Menu.maf?jdeowpBackButtonProtect'
timeout = 10
driver = webdriver.Ie('/Users/USER/\Desktop/IE3')
driver.implicitly_wait(5)
driver.get(NAVER)
LOGIN_INFO = {
    'userId': 'myidid',
    'userPassword': 'mypassword123'
}

driver.find_element_by_name('User').send_keys('swl21803')
driver.find_element_by_xpath('//*[@id="F1"]/table/tbody/tr[8]/td[2]/input').click()
# wait = WebDriverWait(driver, 10)
# WebDriverWait(driver, timeout).until(
#     EC.presence_of_element_located(('id', 'node9823248'))
# )
driver.find_element_by_id('node9823248').click()