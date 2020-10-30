from django.shortcuts import render, reverse
from .models import Contact
# Main contact page!
def contact_list(request):
    return render(request,'contact_list.html')