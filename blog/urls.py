from django.urls import path, include
from . import views
from .models import Blog
# App name of the blog
# To add the name of the url path to any link, 
# you must use the name "Blog:{whichever path name you need to use}" 
app_name="Blog"

urlpatterns = [
    # url path to the main blog view!
    path('blogs/', views.blog_list, name="blog_list"),
]