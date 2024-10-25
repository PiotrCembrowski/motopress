from django.contrib import admin
from django.urls import path
from core.views import frontpage, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('', frontpage, name='frontpage'),
]
