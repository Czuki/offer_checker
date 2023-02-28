from requests_html import HTMLSession


class RequestsEngine:

    _session = None
    _response = None

    def __init__(self, user_product, site_mixin):
        self.user_product = user_product
        self.site_mixin = site_mixin

    @property
    def session(self):
        if self._session is None:
            self._session = HTMLSession()
        return self._session

    @property
    def response(self):
        if self._response is None:
            self._response = self.get_response()
        return self._response

    def get_response(self):
        return self.session.get(self.user_product.product_url)

    def get_element(self, selector):
        return self.response.html.xpath(selector)

    def get_price(self, selector):
        element = self.get_element(selector)
        return self.site_mixin.extract_price(element)

    def get_image(self, selector):
        element = self.get_element(selector)
        return self.site_mixin.extract_image(element)
