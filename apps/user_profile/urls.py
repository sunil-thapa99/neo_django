from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

app_name = 'user_profile'
urlpatterns = [
	# Class method as path takes view.method
	# Passing kwargs used for multiple change.. see the import class in github link
	# https://github.com/django/django/blob/master/django/contrib/auth/views.py
	# path('login/', LoginView.as_view( **{'template_name': 'login.html'})),
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
]
