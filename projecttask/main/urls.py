from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='abouttwo'),
    path('geography-us', views.geography, name='geograf'),
]