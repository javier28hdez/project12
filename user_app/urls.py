from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

from .controllers.views.viewsAccount import registration_view, login_view, logout_view


urlpatterns = [

    #Genera token
    path('api-token-auth/', views.obtain_auth_token),
    
    #Path de la logica del login
    path('register/', registration_view , name="register"),
    path('login/', login_view, name="login"),
    path('logout/',  logout_view, name="logout")
]