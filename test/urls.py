from .views import *
from django.urls import path

app_name = 'test'

urlpatterns = [
    path('posts/', PostListView.as_view()),
]