from django import forms
from .models import Enquiry,AdminLogin


class EnquiryForm(forms.ModelForm):
    
    class Meta:
        model = Enquiry
        fields = "__all__"


class AdminForm(forms.ModelForm):

    class Meta:
        model = AdminLogin
        fields = "__all__"