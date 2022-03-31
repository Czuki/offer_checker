from django.contrib import admin
from django.urls import path, include

import checker.views as checker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', checker_views.DashboardView.as_view(), name='dashboard'),
    path('show-pages/', checker_views.ShowPagesView.as_view(), name='show-pages'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', checker_views.UserRegistrationView.as_view(), name='registration'),
]
