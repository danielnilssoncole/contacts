from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from contacts.models import Contact
from contacts.forms import ContactForm

def index(request):
    contact_list = Contact.objects.order_by('-created_at')[:5]
    context = {'contacts': contact_list}
    return render(request, 'contacts/index.html', context=context)

def show_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    context = {'contact': contact,
               'full_name': contact.full_name,
               'phone_number': contact.phone_number,
               'email': contact.email,
               'created_at': contact.created_at,
               'updated_at': contact.updated_at}
    return render(request, 'contacts/contact.html', context)

def add_contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.full_name = '{0} {1}'.format(contact.first_name, contact.last_name)
            contact.save()
            return HttpResponseRedirect(reverse('contacts:index'))
        else:
            print(form.errors)
    context = {'form' : form}
    return render(request, 'contacts/add_contact.html', context)
