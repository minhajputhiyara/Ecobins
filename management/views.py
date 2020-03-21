from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductUploadForm

from .models import Garbage
from accounts.models import MyUser


@login_required
def UploadGarbageView(request):

    context=dict()
    if request.method=="POST":
        form=ProductUploadForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.uploaded_by=request.user.id
            obj.save()
            messages.add_message(request, messages.SUCCESS,  'Your Waste Posted successfully it will be published after acknowledgement')
        return redirect('homepage')

    else:
        if 2==request.user.account_type:
            messages.add_message(request, messages.ERROR,  'Your Account is Buyer type please create a seller type Account')
            return redirect('homepage')
        form=ProductUploadForm()
        context['upload_form']=form
    return render(request,'publish_waste.html',context)


#display all garbage view is here

def DisplayWasteView(request):

    context=dict()
    active_garbages=Garbage.objects.filter(status=True)
    context['garbages']=active_garbages
    context['loop_times'] = range(1, 4)
    return render(request,'display_waste.html',context)



def BuyGarbageView(request,slug=None,id=None):

    context=dict()
    garbage=Garbage.objects.get(pk=id)
    owner=MyUser.objects.get(pk=garbage.uploaded_by)
    garbage.status=False
    garbage.save()
    context['garbage']=garbage
    context['owner']=owner
    return render(request,'garbage_buy.html',context)