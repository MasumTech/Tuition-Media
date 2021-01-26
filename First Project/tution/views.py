from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           form.save() 
           form = ContactForm() 
           
    else:
        form = ContactForm()   
    return render(request, 'contact.html', {'form':form})    