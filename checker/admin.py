from django.contrib import admin
from checker.models import OriginSite, CheckerProduct


@admin.register(OriginSite)
class OriginSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(CheckerProduct)
class UserPageAdmin(admin.ModelAdmin):
    pass
