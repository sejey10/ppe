from django.urls import path
from . import views


urlpatterns = [
    # home urls
	path('', views.home, name='home'),

    # equipment urls
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('show_all_equipment/', views.show_all_equipment, name='show_all_equipment'),


]