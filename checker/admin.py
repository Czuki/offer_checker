from django.contrib import admin
from checker import models


@admin.register(models.OriginSite)
class OriginSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CheckerProduct)
class UserPageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PriceChangeHistory)
class UserPageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SiteSelector)
class UserPageAdmin(admin.ModelAdmin):
    pass

