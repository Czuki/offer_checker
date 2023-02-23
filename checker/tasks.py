import datetime

from offer_checker.celery import app
from requests_html import HTMLSession
from checker.models import CheckerProduct, PriceChangeHistory

import logging

log = logging.getLogger(__name__)


@app.task(bind=True)
def update_product_price_requests_task(self, user_product_id):
    session = HTMLSession()
    user_product = CheckerProduct.objects.get(pk=user_product_id)
    response = session.get(user_product.product_url)
    price = response.html.xpath(user_product.origin_site.site_selector.price_selector_xpath)

    current_price = price[0].attrs['content']

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
def update_product_image_requests_task(self, user_product_id):
    session = HTMLSession()
    user_product = CheckerProduct.objects.get(pk=user_product_id)
    response = session.get(user_product.product_url)

    image = response.html.xpath(user_product.origin_site.site_selector.image_selector_xpath)
    image_src = image[0].attrs['content']

    user_product.product_image_url = image_src
    user_product.save()
