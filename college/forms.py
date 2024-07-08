from django import forms
from .models import Enquiry
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields="__all__" ## for all fields
        # fields=["name","email","phone","query"] ##for specific fields