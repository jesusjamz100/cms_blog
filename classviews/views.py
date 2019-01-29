from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

class ContactList(ListView):
	model = Contact

class ContactDetail(DetailView):
	model = Contact

class ContactCreate(CreateView):
	model = Contact
	fields = ('name', 'email', 'address', 'phone')
	succes_url = reverse_lazy('contact_list')

class ContactUpdate(UpdateView):
	model = Contact
	fields = ('name', 'email', 'address', 'phone')
	success_url = reverse_lazy('contact_list')

class ContactDelete(DeleteView):
	model = Contact