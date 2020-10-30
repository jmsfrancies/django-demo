from django.urls import path, include
from . import views

urlpatterns = [
    path('blog/', views.blog_list, name="blog_list"),
]