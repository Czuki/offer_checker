import datetime

from offer_checker.celery import app

from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.common.exceptions import NoSuchElementException
from checker.models import CheckerProduct, PriceChangeHistory

import logging

log = logging.getLogger(__name__)

def get_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='http://192.168.0.102:4444/wd/hub', options=options)
    return driver


@app.task(bind=True)
def update_product_price_task(self, user_product_id):
    driver = get_driver()
    user_product = CheckerProduct.objects.get(pk=user_product_id)
    try:
        driver.get(user_product.product_url)
        try:
            price = driver.find_element(By.XPATH, '//meta[@property="product:sale_price:amount"]')
        except NoSuchElementException:
            price = driver.find_element(By.XPATH, '//meta[@property="product:price:amount"]')
        current_price = price.get_attribute('content')
        driver.quit()
    except Exception as exc:
        print(exc)
        driver.quit()
        return False

    user_product.previous_price = user_product.current_price
    user_product.current_price = current_price

    if user_product.previous_price != user_product.current_price:
        user_product.price_change_date = datetime.datetime.now()

    user_product.save()

    if user_product.previous_price:
        price_diff = float(user_product.current_price) - float(user_product.previous_price)
        PriceChangeHistory.objects.create(
            product=user_product,
            previous_price=user_product.previous_price,
            new_price=user_product.current_price,
            price_difference=price_diff,
        )


@app.task(bind=True)
def update_product_image_task(self, user_product_id):
    driver = get_driver()
    user_product = CheckerProduct.objects.get(pk=user_product_id)
    try:
        driver.get(user_product.product_url)
        image = driver.find_element(By.XPATH, '//meta[@property="og:image"]')
        image_src = image.get_attribute('content')
        driver.quit()
    except Exception:
        driver.quit()
        return False
    print(image_src)
    user_product.product_image_url = image_src
    user_product.save()




