from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'), #add views here
    path('about/', views.about, name = 'about'),
    path('submit/', views.submit, name ='submit')
]
