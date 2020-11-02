from django.shortcuts import render, reverse
from .models import Blog
from contact.views import *
# Main blog app view that displays the list of views!
def blog_list(request):
    blogs = Blog.objects.order_by('-pub_date')[:5]
    return render(request,'blog_list.html', {'blogs':blogs})