from django.contrib import admin
from django.urls import path
from core.views import frontpage, contact, post, article
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'motopress'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('post/', post, name='post'),
    path('', frontpage, name='frontpage'),
    path('<slug:slug>/', article, name="article"),
    path("__reload__/", include("django_browser_reload.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
