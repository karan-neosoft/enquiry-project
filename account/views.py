from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Enquiry,AdminLogin
from .forms import EnquiryForm,AdminForm
from django.core.paginator import Paginator

# all enquiry form data rendered here
def account(request):
    """ Render all records of enquiry form  """

    if request.session.get('username')=="karan":
        all_records = Enquiry.objects.all()
        paginator = Paginator(all_records,2)
        page = request.GET.get('page')
        all_records = paginator.get_page(page)
        return render(request,'records.html',{"data":all_records})
    return redirect('/enquiry')


# edit option for the admin to edit enquiry data which is render
def edit_data(request,id):
    """ Show the data for edit in form """

    if request.session.get('username')=="karan":
        enquiry_data = Enquiry.objects.get(id=id)  
        return render(request,'admin_enquiry_form.html', {'data':enquiry_data})
    return redirect('/enquiry')


#edit data action performed here after submit button is clicked
def edit_data_updated(request):
    """ Edit data validation and insert into database """

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


#delete  user data
def delete_data(request,id):
    """ Delete user data """

    if request.session.get('username')=="karan":
        Enquiry.objects.filter(id=id).delete()
        return redirect("/")
    return redirect('/enquiry')


#login panel for admin
def login(request):
    """ render of the login panel page """

    return render(request,'login.html')


#login check for admin panel
def login_action(request):
    """ Login form validation check """

    formdata = request.POST.dict()

    try:
        result = AdminLogin.objects.get(password=formdata['password'],username=formdata['username'])
        request.session['username'] = formdata['username']
        return JsonResponse({"status":"Login successfully","flag":1})
    except AdminLogin.DoesNotExist:
        return JsonResponse({"status":"Invalid credentials","flag":0})

#logout from admin panel
def logout(request):
    username = request.session.get('username')
    if username is not None:
        del request.session['username']
        return redirect('/login')
        # return JsonResponse({"success":"User logged out"})