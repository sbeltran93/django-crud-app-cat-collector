from django.urls import path
from . import views

urlpatterns = [
    #routes will be added here
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index')
]