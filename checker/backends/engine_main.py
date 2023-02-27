from checker.models import OriginSite
from checker.backends.playwright_engine import PlaywrightEngine
from checker.backends.requests_engine import RequestsEngine


class ScrapeEngine:

    _engine = None

    def __init__(self, user_product):
        self.user_product = user_product
        self.scraping_engine = user_product.origin_site.scraping_engine

    @property
    def engine(self):
        if self._engine is None:
            if self.scraping_engine == OriginSite.REQUESTS_HTML_ENGINE:
                self._engine = RequestsEngine(self.user_product)
            elif self.scraping_engine == OriginSite.PLAYWRIGHT_ENGINE:
                self._engine = PlaywrightEngine(self.user_product)
            else:
                raise ValueError('Value for scraping engine not set')
        return self._engine

    def get_price(self):
        selector = self.user_product.origin_site.site_selector.price_selector_xpath
        return self.engine.get_price(selector)

    def get_image(self):
        selector = self.user_product.origin_site.site_selector.image_selector_xpath
        return self.engine.get_image(selector)
