from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Czas utworzenia',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Czas aktualizacji',
    )

    class Meta:
        abstract = True


class SiteSelector(BaseModel):
    price_selector_xpath = models.TextField(
        blank=True,
        null=True,
        verbose_name='Selektor cen xpath'
    )
    image_selector_xpath = models.TextField(
        blank=True,
        null=True,
        verbose_name='Selektor obrazu xpath'
    )
    price_selector_css = models.TextField(
        blank=True,
        null=True,
        verbose_name='Selektor cen css'
    )
    image_selector_css = models.TextField(
        blank=True,
        null=True,
        verbose_name='Selektor obrazu css'
    )

    def __str__(self):
        return 'Site Selector {}'.format(self.pk)


class OriginSite(BaseModel):
    name = models.CharField(
        max_length=32,
        verbose_name='Nazwa',
    )
    main_url = models.CharField(
        max_length=256,
        verbose_name='Strona główna',
    )
    site_selector = models.ForeignKey(
        'SiteSelector',
        on_delete=models.CASCADE,
        verbose_name='Selektory strony',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Strona główna'
        verbose_name_plural = 'Strony główne'

    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)


class CheckerProduct(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Użytkownik',
    )
    origin_site = models.ForeignKey(
        OriginSite,
        on_delete=models.CASCADE,
        verbose_name='Strona źródłowa',
    )
    product_url = models.CharField(
        max_length=512,
        verbose_name='Link do produktu',
    )
    name = models.CharField(
        max_length=64,
        verbose_name='Nazwa produktu'
    )
    previous_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Poprzednia cena produktu',
        null=True, blank=True,
    )
    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Aktualna cena produktu',
        null=True, blank=True,
    )
    price_change_date = models.DateTimeField(
        verbose_name='Data zmiany ceny',
        null=True, blank=True,
    )
    product_image_url = models.CharField(
        max_length=512,
        verbose_name='Link do zdjęcia produktu',
        null=True, blank=True,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Produkt do śledzenia'
        verbose_name_plural = 'Produkty do śledzenia'

    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)


class PriceChangeHistory(BaseModel):

    product = models.ForeignKey(
        CheckerProduct,
        on_delete=models.CASCADE,
        verbose_name='Produkt',
    )
    previous_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Poprzednia cena produktu',
        null=True, blank=True,
    )
    new_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Nowa cena produktu',
        null=True, blank=True,
    )
    price_difference = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Różnica w cenie',
        null=True, blank=True,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Historia zmian cen'
        verbose_name_plural = 'Historia zmian cen'

    def __str__(self):
        return 'PriceDifference {}'.format(self.price_difference)
