from django.http import HttpResponseRedirect
from django.shortcuts import render
from website.forms import ContactForm,NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request,"website/index.html")

def about_view(request):
    return render(request,"website/about.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.add_message(request,messages.SUCCESS,'your message successfully send :)')
        else:
            messages.add_message(request,messages.ERROR,'your message didnt send :(')
    form = ContactForm()
    return render(request,"website/contact.html",{"form":form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
        
        
    
 
    
            