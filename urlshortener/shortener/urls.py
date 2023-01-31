from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from shortener import views as shortener_views

router = routers.DefaultRouter()

router.register(r"shortener", shortener_views.URLShortenerViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls
