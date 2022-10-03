import django
from django.urls import path
from . import views
urlpatterns = [
    path('', views.MyTemplateView.as_view(), name='home'),
]

