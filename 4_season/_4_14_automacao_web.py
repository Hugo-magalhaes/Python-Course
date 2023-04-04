from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


# headless - executa sem abrir o chrome
chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROME_DRIVER))
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
)

chrome_browser.get('https://www.google.com/')
search_input = WebDriverWait(chrome_browser, 10).until(
    ec.presence_of_element_located((By.NAME, 'q')
                                   )
)
search_input.send_keys('Hello world')
search_input.send_keys(Keys.ENTER)

results = chrome_browser.find_element(By.ID,  'search')
links = results.find_elements(By.TAG_NAME,  'a')
links[0].click()

sleep(10)
