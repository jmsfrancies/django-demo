from django.shortcuts import render, reverse
from .models import Blog
# Main blog app view that displays the list of views!
def blog_list(request):
    return render(request,'blog_list.html')