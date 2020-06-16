from django.urls import path
from . import views


urlpatterns = [
    # home urls
	path('', views.home, name='home'),

    # equipment urls
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('show_all_equipment/', views.show_all_equipment, name='show_all_equipment'),
    path('use_equipment/', views.use_equipment, name='use_equipment'),
    path('dispose_equipment/<int:id>', views.dispose_equipment, name='dispose_equipment'),
    path('detailed_equipment/<int:id>', views.detailed_equipment, name='detailed_equipment'),

    path('dispose_package/<int:pk>', views.dispose_package, name='dispose_package'),
    path('update_package/<int:pk>', views.update_package, name='update_package')



]