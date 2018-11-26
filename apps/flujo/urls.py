from django.urls import path

from apps.flujo import views


urlpatterns = [
   path('home', views.Home.as_view(), name='view_home'),
]