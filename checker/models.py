from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OriginSite(BaseModel):
    name = models.CharField(max_length=32)
    main_url = models.CharField(max_length=256)

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
    )
    origin_site = models.ForeignKey(
        OriginSite,
        on_delete=models.CASCADE
    )
    page_url = models.CharField(max_length=512)
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Strona użytkownika'
        verbose_name_plural = 'Strony użytkownika'

    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)

