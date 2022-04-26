from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from .views import registration_view


urlpatterns = [
    path('register/', registration_view, name='register'),
    # api/token is same as login.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # used to get access token by providing refresh token.
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
