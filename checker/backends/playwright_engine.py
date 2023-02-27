from playwright.sync_api import sync_playwright


class PlaywrightEngine:
    # TODO(Getting random user agent from external file)
    # TODO(Figure out better way to handle sync_playwright context manager)

    def __init__(self, user_product):
        self.user_product = user_product

    def get_price(self, selector):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
            )
            page.goto(self.user_product.product_url)
            locator = 'xpath={}'.format(selector)
            element = page.locator(locator)
            price = element.get_attribute('content')
            browser.close()
        return price

    def get_image(self, selector):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
            )
            page.goto(self.user_product.product_url)
            locator = 'xpath={}'.format(selector)
            element = page.locator(locator)
            image = element.get_attribute('content')
            browser.close()
        return image
