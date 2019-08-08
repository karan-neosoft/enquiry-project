from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Enquiry,AdminLogin
from .forms import EnquiryForm,AdminForm


def account(request):
    if request.session.get('username')=="karan":
        all_records = Enquiry.objects.all()
        return render(request,'records.html',{"data":all_records})
    return redirect('/enquiry')


def edit_data(request,id):
    if request.session.get('username')=="karan":
        enquiry_data = Enquiry.objects.get(id=id)  
        return render(request,'admin_enquiry_form.html', {'data':enquiry_data})
    return redirect('/enquiry')

def edit_data_updated(request):
    if request.session.get('username')=="karan":
        form_data = request.POST.dict()
        validity_status = EnquiryForm(form_data)
        if not validity_status.is_valid():
            print(validity_status)
            return JsonResponse(validity_status.errors)
        else:
            unique_id = form_data['id']
            form_data.pop('id')
            Enquiry.objects.filter(pk=unique_id).update(**form_data)
            return JsonResponse({"status":"Data Updated Successfully"})
    return redirect('/enquiry')


def delete_data(request,id):
    if request.session.get('username')=="karan":
        Enquiry.objects.filter(id=id).delete()
        return redirect("/")
    return redirect('/enquiry')


def login(request):
    return render(request,'login.html')


def login_action(request):
    formdata = request.POST.dict()

    try:
        result = AdminLogin.objects.get(password=formdata['password'],username=formdata['username'])
        request.session['username'] = formdata['username']
        return JsonResponse({"status":"Login successfully","flag":1})
    except AdminLogin.DoesNotExist:
        return JsonResponse({"status":"Invalid credentials","flag":0})
