from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from datetime import datetime
CHROME_DRIVER = './chromedriver'
FIREFOX_DRIVER = './geckodriver'
import time
import re
import json
import random

##starting views are 187, 72, 49

def setup_driver(headless=False, driver_type=CHROME_DRIVER):
    if 'chrome' in driver_type.lower():
        options = ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')

        if headless:
            options.add_argument('-headless')
        driver = webdriver.Chrome(executable_path=driver_type, chrome_options=options)
    else:
        options = FirefoxOptions()
        if headless:
            options.add_argument('-headless')
        driver = webdriver.Firefox(executable_path=driver_type, firefox_options=options)

    return driver


def setup_enviroment(driver, url):
    actions = ActionChains(driver)
    driver.get(url)
    time.sleep(4)
    actions.send_keys("m").perform()
    time.sleep(4)
    executing_query1 = 'document.getElementById("toggleBar").click()'
    driver.execute_script(executing_query1)
    time.sleep(3)
    executing_query2 = 'document.getElementsByClassName("ytp-button ytp-settings-button")[0].click()'
    driver.execute_script(executing_query2)
    time.sleep(3)
    executing_query3 = 'document.getElementsByClassName("ytp-menuitem")[3].click()'
    driver.execute_script(executing_query3)
    time.sleep(3)
    executing_query4 = 'document.getElementsByClassName("ytp-menuitem")[7].click()'
    driver.execute_script(executing_query4)
    time.sleep(3)

   

def get_soup(driver, url):
    actions = ActionChains(driver)
    driver.get(url)
    time.sleep(4)
    # actions.send_keys(Keys.SPACE).perform()
    # time.sleep(4)
    

def run():
    driver = setup_driver()
    cont = True
    urls = ['https://www.youtube.com/watch?v=Hp4xjixyUVA', 'https://www.youtube.com/watch?v=wX5Sj5NAZ4o', 'https://www.youtube.com/watch?v=M9gqND4R6uU&t=268s']
    durations = [114, 182, 482]
    plays = [0, 0, 0]
    setup_enviroment(driver, urls[0])
    while(cont):
        for i, url in enumerate(urls):
            get_soup(driver, url)
            time.sleep(durations[i])
            plays[i] += 1
            print ("done with link " + str(i+1))
            if i == 2:
                print(plays)
           