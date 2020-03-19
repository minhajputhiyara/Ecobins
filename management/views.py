from django.shortcuts import render,redirect
from .forms import ProductUploadForm




def UploadGarbageView(request):

    context=dict()
    if "POST"==request.method:
        pass

    form=ProductUploadForm()
    context['upload_form']=form

    return render(request,'upload_garbage.html',context)
