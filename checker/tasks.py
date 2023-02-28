from django.utils import timezone

from offer_checker.celery import app
from checker.models import CheckerProduct, PriceChangeHistory
from checker.backends.engine_main import ScrapeEngine


import logging

log = logging.getLogger(__name__)


@app.task(bind=True)
def send_price_change_notification(self, user_product_name, user_product_url, price_diff, email):
    from checker.mailer import Mailer
    Mailer().send_notification(
        user_product_name=user_product_name,
        user_product_url=user_product_url,
        price_diff=price_diff,
        user_mail=email
    )


@app.task(bind=True)
def update_product_price_requests_task(self, user_product_id):
    user_product = CheckerProduct.objects.get(pk=user_product_id)
    current_price = ScrapeEngine(user_product).get_price()
    user_product.previous_price = user_product.current_price
    user_product.current_price = current_price

    if user_product.previous_price != user_product.current_price:
        user_product.price_change_date = timezone.now()

    user_product.save()
    user_product.refresh_from_db()

    if user_product.previous_price:
        price_diff = user_product.previous_price - user_product.current_price
        if price_diff > 0:
            send_price_change_notification.apply_async(
                kwargs={
                    'user_product_name': user_product.name,
                    'user_product_url': user_product.product_url,
                    'price_diff': price_diff,
                    'email': user_product.user.email
                }
            )

        PriceChangeHistory.objects.create(
            product=user_product,
            previous_price=user_product.previous_price,
            new_price=user_product.current_price,
            price_difference=price_diff,
        )
    return 'Extracted price: {}'.format(current_price)


@app.task(bind=True)
def update_product_image_requests_task(self, user_product_id):
    user_product = CheckerProduct.objects.get(pk=user_product_id)
    image_src = ScrapeEngine(user_product).get_image()

    user_product.product_image_url = image_src
    user_product.save()

    return 'Extracted image: {}'.format(image_src)

