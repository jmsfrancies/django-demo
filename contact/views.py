from django.shortcuts import render, reverse
from .models import Contact
# Main contact page!
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request,'contact_list.html', {'contacts':contacts})