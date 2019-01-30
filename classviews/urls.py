from django.urls import path
from . import views

app_name = "classview"

urlpatterns = [
    # [...]
    path('', views.ContactList.as_view(), name='contact_list'),
    path('contact/<int:pk>/', views.ContactDetail.as_view(), name='contact_detail'),
    path('create/', views.ContactCreate.as_view(), name='contact_create'),
    path('update/<int:pk>/', views.ContactUpdate.as_view(), name='contact_edit'),
    path('delete/<int:pk>/', views.ContactDelete.as_view(), name='contact_delete'),
]