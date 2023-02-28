from checker.models import OriginSite


class BaseSite:

    def __init__(self, engine_type):
        self.engine_type = engine_type

    def requests_extract_price(self, element):
        raise NotImplementedError

    def playwright_extract_price(self, element):
        raise NotImplementedError

    def requests_extract_image(self, element):
        raise NotImplementedError

    def playwright_extract_image(self, element):
        raise NotImplementedError

    def extract_price(self, element):
        if self.engine_type == OriginSite.REQUESTS_HTML_ENGINE:
            return self.requests_extract_price(element)
        elif self.engine_type == OriginSite.PLAYWRIGHT_ENGINE:
            return self.playwright_extract_price(element)

    def extract_image(self, element):
        if self.engine_type == OriginSite.REQUESTS_HTML_ENGINE:
            return self.requests_extract_image(element)
        elif self.engine_type == OriginSite.PLAYWRIGHT_ENGINE:
            return self.playwright_extract_image(element)


class MediaMarktSite(BaseSite):

    def requests_extract_price(self, element):
        return element[0].attrs['content']

    def playwright_extract_price(self, element):
        return element.get_attribute('content')

    def requests_extract_image(self, element):
        return element[0].attrs['content']

    def playwright_extract_image(self, element):
        return element.get_attribute('content')


class MediaExpertSite(BaseSite):

    def requests_extract_price(self, element):
        return element[0].attrs['content']

    def playwright_extract_price(self, element):
        return element.get_attribute('content')

    def requests_extract_image(self, element):
        return element.get_attribute('content')

    def playwright_extract_image(self, element):
        return element.get_attribute('content')
