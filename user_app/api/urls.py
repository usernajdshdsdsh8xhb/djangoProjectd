
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import CustomAuthToken, registration_view

urlpatterns = [
    path("login/", CustomAuthToken.as_view()),
    path("register/", registration_view)

]