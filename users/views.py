from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render

from users.forms import CustomUserCreationForm


def user_home(request):
	template_name = 'users/index.html'

	return render(request, template_name, context=None)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'