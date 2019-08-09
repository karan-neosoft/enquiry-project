from . import views 
from django.urls import path


urlpatterns = [
    path('',views.index,name='enquiry-form'),
    path('enquiry-submit',views.enquiry_form_action)
]
