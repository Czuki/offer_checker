from checker.models import OriginSite
from checker.backends.playwright_engine import PlaywrightEngine
from checker.backends.requests_engine import RequestsEngine
from checker.sites import MediaMarktSite, MediaExpertSite


class ScrapeEngine:

    _engine = None
    _site_mixin = None

    def __init__(self, user_product):
        self.user_product = user_product
        self.scraping_engine = user_product.origin_site.scraping_engine

    @property
    def site_mixin(self):
        if self._site_mixin is None:
            if self.user_product.origin_site.name == 'MediaMarkt':
                self._site_mixin = MediaMarktSite
            if self.user_product.origin_site.name == 'MediaExpert':
                self._site_mixin = MediaExpertSite
        return self._site_mixin

    @property
    def engine(self):
        if self._engine is None:
            if self.scraping_engine == OriginSite.REQUESTS_HTML_ENGINE:
                self._engine = RequestsEngine(self.user_product, self.site_mixin(OriginSite.REQUESTS_HTML_ENGINE))
            elif self.scraping_engine == OriginSite.PLAYWRIGHT_ENGINE:
                self._engine = PlaywrightEngine(self.user_product, self.site_mixin(OriginSite.PLAYWRIGHT_ENGINE))
            else:
                raise ValueError('Value for scraping engine not set')
        return self._engine

    def get_price(self):
        selector = self.user_product.origin_site.site_selector.price_selector_xpath
        return self.engine.get_price(selector)

    def get_image(self):
        selector = self.user_product.origin_site.site_selector.image_selector_xpath
        return self.engine.get_image(selector)
