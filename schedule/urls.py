from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import re_path
from django.contrib.staticfiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('authentication.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]
