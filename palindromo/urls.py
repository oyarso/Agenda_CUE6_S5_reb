from django.urls import path 
from .views import IndexPageView, esPalindromo
urlpatterns = [ 
path("", IndexPageView.as_view(), name="index"), 
path("palindromo/<name>", esPalindromo, name="palindromo"), ]