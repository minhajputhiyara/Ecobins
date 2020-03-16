from django.shortcuts import render,redirect
from .forms import UserCreationForm,UserChangeForm
# Create your views here.




def HomeView(request):

    return render(request,'test1.html')

def SignUpView(request):
    context={}
    if request.method=="POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('homepage')


    
    context['signup_form']=UserCreationForm()

    return render(request,'test2.html',context)