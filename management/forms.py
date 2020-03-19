from django.forms import ModelForm
from .models import Garbage





class ProductUploadForm(ModelForm):

    class Meta:
        model=Garbage
        fields='__all__'
        exclude=['uploaded_by','slug','status',]