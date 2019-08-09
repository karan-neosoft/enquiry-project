from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .forms import EnquiryForm
from .models import Enquiry

# enquiry form UI render
def index(request):
    """ Enquiry form UI render """

    return render(request,'enquiry_form.html')


# enquiry form data validation and insert into database
def enquiry_form_action(request):
    """ Enquiry form validation and insert operation """
    
    form_data = request.POST.dict()
    validity_status = EnquiryForm(form_data)
    if not validity_status.is_valid():
        return JsonResponse(validity_status.errors)
    else:
        Enquiry.objects.create(**form_data)
        return JsonResponse({"status":"Success"})