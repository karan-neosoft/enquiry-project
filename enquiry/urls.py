from . import views 
from django.urls import path


urlpatterns = [
    path('',views.index),
    path('enquiry-submit',views.enquiry_form_action)
]
