from django.contrib import admin
from django.urls import path
from core.views import frontpage, contact
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('', frontpage, name='frontpage'),
    path("__reload__/", include("django_browser_reload.urls"))
]
