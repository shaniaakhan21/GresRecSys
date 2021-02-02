from django.urls import path 
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('home/',views.front , name='front'),
    path('about/',views.contact , name='contact'),
    path('video/', views.reco , name='reco')
]