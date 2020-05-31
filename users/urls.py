from django.urls import path
from .views import SignUpView, user_home


urlpatterns = [
    path('', user_home, name='user_home'),

    path('signup/', SignUpView.as_view(), name='signup'),

]