from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import register_view,logout_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('login/',obtain_auth_token, name='login'),
    path('registration/',register_view, name='register_user'),
    path('logout/',logout_view, name='logout_view'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
