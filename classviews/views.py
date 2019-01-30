from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse
from .models import *


class ContactList(ListView):
	model = Contact


class ContactDetail(DetailView):
	model = Contact


class ContactCreate(CreateView):
    model = Contact
    fields = ('name', 'email', 'address', 'phone')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Contact has been registered')
        return reverse('classview:contact_list')


class ContactUpdate(UpdateView):
    model = Contact
    fields = ('name', 'email', 'address', 'phone')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Contact has been registered')
        return reverse('classview:contact_list')

class ContactDelete(DeleteView):
    model = Contact

	# send the user back to their own page after a successful update
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'El cliente ha sido eliminado satisfactoriamente')
        return reverse('classview:contact_list')

