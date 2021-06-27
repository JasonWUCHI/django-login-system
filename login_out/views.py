from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest
from login_out.forms import loginForm , registerForm
from .models import Profile
from django.contrib.auth import get_user_model, authenticate, login , logout
from django.contrib.auth.decorators import login_required
User = get_user_model()

# Create your views here.
def index(request):
    return render(request , 'index.html')

def loginView(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request , username = username , password = password)

        if user != None:
            login(request , user)
            return HttpResponseRedirect('../inner/')
        else:
            pass
            #some effect
    context = {
        'form' : form
    }
    return render(request , 'login_forms.html' , context = context)

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('../')

def registerView(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        prefer_name = form.cleaned_data.get('prefer_name')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        school = form.cleaned_data.get('school')
        gender = form.cleaned_data.get('gender')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        

        try:
            user = User.objects.create_user(username = email , email = email ,password = password)
        except:
            user = None
        
        if user != None:
            profile = Profile(user = user , first_name = first_name , last_name = last_name , school = school , gender = gender , prefer_name = prefer_name)
            profile.save()
            login(request , user)

            return HttpResponseRedirect('../inner/')
        else:
            pass
    context = {
        'form' : form
    }
    return render(request , "register_forms.html" , context = context)

@login_required
def innerPageView(request):
    return render(request , 'inner.html')





