from django.shortcuts import render

# Create your views here.
def contact_list(request):
    return render(request,'contact_list.html')