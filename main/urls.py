from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.buypage, name='buypage'),
    path('about/', views.about, name='about'),
]