from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.contact_list, name="contact_list"),
]