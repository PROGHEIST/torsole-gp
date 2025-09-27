from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import GramPanchayatInfoViewSet, SlideShowViewSet

router = routers.DefaultRouter()
router.register('gpinfo', GramPanchayatInfoViewSet)
router.register('slideshow', SlideShowViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)