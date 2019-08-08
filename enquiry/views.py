from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .forms import EnquiryForm
from .models import Enquiry
def index(request):
    return render(request,'enquiry_form.html')


def enquiry_form_action(request):
    form_data = request.POST.dict()
    validity_status = EnquiryForm(form_data)
    if not validity_status.is_valid():
        print(validity_status)
        return JsonResponse(validity_status.errors)
    else:
        Enquiry.objects.create(**form_data)
        return JsonResponse({"status":"Success"})