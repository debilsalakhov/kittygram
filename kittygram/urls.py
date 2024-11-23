from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from django.urls import path, include

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet, basename='CreateRetrieveCats')

urlpatterns = [
   path('', include(router.urls)),
   path('api-token-auth/', views.obtain_auth_token),
]
