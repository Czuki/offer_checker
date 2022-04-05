import time

from offer_checker.celery import app

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from bs4 import BeautifulSoup
import json

from checker.models import CheckerProduct

@app.task(bind=True)
def debug_task(self):

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # driver = webdriver.Chrome(
    #     options=options,
    #     executable_path=r"C:\Users\Bartosz\Desktop\WORKSPACE\offer_checker\chromedriver.exe"
    # )
    driver = webdriver.Remote(command_executor='http://localhost:4444', options=options)

    driver.get('https://www.mediaexpert.pl/agd-male/zdrowie-i-uroda/pulsoksymetry/pulsoksymetr-oromed-oro-pulse-black')
    # price = driver.find_element_by_class_name('main-price').get_attribute('innerText')
    scripts = driver.find_elements(By.CSS_SELECTOR, "script[type='application/ld+json']")
    product_data_json = json.loads(scripts[0].get_attribute('innerText'))
    print(product_data_json)
    # print(scripts[0].get_attribute('innerText'))
    # needed = []
    # for script in scripts:
    #     if script.get_attribute('type') == 'application/ld+json':
    #         needed.append(script)
    driver.quit()
    return 'price'


@app.task(bind=True)
def update_product_price_task(self, user_product_id):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(
    #     options=options,
    #     executable_path=r"C:\Users\Bartosz\Desktop\WORKSPACE\offer_checker\chromedriver.exe"
    # )
    driver = webdriver.Remote(command_executor='http://localhost:4444', options=options)
    options.add_argument("--start-maximized")

    try:
        user_product = CheckerProduct.objects.get(pk=user_product_id)
        driver.get(user_product.product_url)
        time.sleep(40)
        driver.quit()
    except CheckerProduct.DoesNotExist:
        return False



