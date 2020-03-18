from django.shortcuts import render,redirect
from .forms import UserCreationForm,UserChangeForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

def HomeView(request):

    return render(request,'base.html')

def SignUpView(request):
    context={}
    if request.method=="POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request, 'Your Account Created Successfully')

            return redirect('homepage')


    
    context['signup_form']=UserCreationForm()

    return render(request,'accounts/signup.html',context)