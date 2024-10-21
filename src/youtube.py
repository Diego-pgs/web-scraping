from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service(ChromeDriverManager().install())
# service = Service(executable_path='./chromedriver')

navegador = webdriver.Chrome(service=service)

navegador.get('https://www.youtube.com')

sleep(2)

box_search = navegador.find_element(By.NAME, 'search_query')

box_search.send_keys('teste')

sleep(2)
box_search.send_keys(Keys.RETURN)

input()
