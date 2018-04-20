from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
        "title":"Hello World!",        
        "content":" Welcome to the homepage."    
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About World!",
        "content":" Welcome to the about page."
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",        
        "content":"Welcome to the contact page.",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
        # print(request.POST)
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form":login_form
    }
    print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
    return render(request, "auth/login.html", context)

def register_page(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        print(register_form.cleaned_data)
    return render(request, "auth/register.html", {})
