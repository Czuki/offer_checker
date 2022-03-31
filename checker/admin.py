from django.contrib import admin
from checker.models import OriginSite, UserPage


@admin.register(OriginSite)
class OriginSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(UserPage)
class UserPageAdmin(admin.ModelAdmin):
    pass
