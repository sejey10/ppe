from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='analytics_home'),
    path('equipment/', views.eqt_analytics, name='analytics_eqt'),
]   