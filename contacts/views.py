from django.shortcuts import render
from contacts.models import Contact

def index(request):
    contact_list = Contact.objects.order_by('-created_at')[:5]
    context = {'contacts': contact_list}
    return render(request, 'contacts/index.html', context=context)
