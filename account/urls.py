from . import views 
from django.urls import path


urlpatterns = [
    path('',views.account),
    path('login',views.login),
    path('login-action',views.login_action),
    path('edit/<int:id>', views.edit_data),
    path('edit/edit-action',views.edit_data_updated),
    path('delete/<int:id>', views.delete_data),
]
