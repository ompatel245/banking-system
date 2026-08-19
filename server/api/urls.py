from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BankDetailsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'bank-details', BankDetailsViewSet, basename='bank-details')

urlpatterns = [
    path('', include(router.urls))
]