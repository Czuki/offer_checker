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


class OriginSite(BaseModel):
    name = models.CharField(
        max_length=32,
        verbose_name='Nazwa',
    )
    main_url = models.CharField(
        max_length=256,
        verbose_name='Strona główna',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Strona główna'
        verbose_name_plural = 'Strony główne'

    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)


class UserPage(BaseModel):
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
    page_url = models.CharField(
        max_length=512,
        verbose_name='Link do produktu',
    )
    name = models.CharField(
        max_length=64,
        verbose_name='Nazwa produktu'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Strona użytkownika'
        verbose_name_plural = 'Strony użytkownika'

    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)
