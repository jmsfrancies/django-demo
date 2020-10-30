from django.urls import path, include
from . import views
from .models import Contact
# App name of the Contact
# To add the name of the url path to any link, 
# you must use the name "Contact:{whichever path name you need to use}" 
app_name= "Contact"

urlpatterns = [
    # url path to the main contact page
    path('', views.contact_list, name="contact_list"),
]