from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.staticfiles import views
from rest_framework.routers import DefaultRouter
from event.views import EventViewset, EventTemplateViewset
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'events', EventViewset, basename='events')

schema_view = get_schema_view(
    openapi.Info(
        title="Apis agenda",
        default_version='v1',
        description="Exemplo de boas praticas utilizando django rest framework",
        terms_of_service="",
        contact=openapi.Contact(email="felipe.alves2014@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('autenticacao/', include('authentication.urls')),
    path('evento/calendario/', EventTemplateViewset.as_view(), name='callendar')
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]
