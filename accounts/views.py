from django.shortcuts import render,redirect
from .forms import UserCreationForm,UserChangeForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required


from .models import  MyUser
from management.views import Garbage
from management.forms import ProductUploadForm

def HomeView(request):

    return render(request,'base.html')

def SignUpView(request,id=None):
    context={}
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if id!=None:
            myuser=MyUser.objects.get(pk=id)
            form=ProductUploadForm(request.POST,instance=myuser)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,  'Your Profile Updated Successfully')
                return redirect('homepage')
            else:
                messages.add_message(request, messages.ERROR,  'Update data is not valid')
                return redirect('homepage')

        else:    
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=raw_password)
                login(request, user)
                messages.success(request, 'Your Account Created Successfully')
                return redirect('homepage')

    else:
        if id!=None:
            myuser=MyUser.objects.get(id=id)
            '''
            print(myuser.username)
            print(myuser)
            print(myuser.email)
            '''
            form=UserCreationForm(instance=myuser)
            context['signup_form']=form
        else:
            form=UserCreationForm()
            context['signup_form']=form

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


@login_required
def ProfileView(request,id=None):

    context=dict()
    myuser=MyUser.objects.get(pk=id)
    context['myuser']=myuser
    if myuser.account_type==1:
        garbages=Garbage.objects.filter(uploaded_by=id)
        context['garbages']=garbages
    return render(request,'accounts/user_profile.html',context)

@login_required

def DeleteGarbageView(request,id=None):
    
    instance = Garbage.objects.get(pk=id)
    instance.delete()
    messages.add_message(request, messages.ERROR,  'Your Garbage deleted !!!')
    return redirect('homepage')