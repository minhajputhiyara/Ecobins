from django.shortcuts import render,redirect
from .forms import UserCreationForm,UserChangeForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout

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


def LogoutView(request):

    logout(request)
    messages.add_message(request, messages.SUCCESS,  'Logged Out Successfully thnaks for beign with us')
    return redirect('homepage')


def LoginView(request):
    context={}
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            messages.add_message(request, messages.SUCCESS,  'You are successfully logged in !!!')
        return redirect('homepage')
    else:
        form=LoginForm()
        context['login_form']=form
    return render(request,'accounts/login.html',context)