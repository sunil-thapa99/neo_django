from django.urls import path

from .views import home

app_name = 'quiz'
urlpatterns = [
    path('', home),
]
