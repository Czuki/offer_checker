from django.core.mail import send_mail


class Mailer:

    def send_notification(self, user_product_name, user_product_url, price_diff, user_mail):

        subject = 'Offer Checker Notification'
        message = f'Price for {user_product_name}: {user_product_url} has changed by: {price_diff}'
        send_mail(
            subject,
            message,
            'from@example.com',
            [user_mail],
            fail_silently=False,
        )
