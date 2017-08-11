import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'contacts_project.settings')

import django
django.setup()
from contacts.models import Contact

def populate():
    contact1 = {
        'first_name': 'Loston',
        'last_name': 'Fondon',
        'phone_number': 8131234567,
        'email': 'lostonf@gmail.com'
    }
    contact2 = {
        'first_name': 'Trent',
        'last_name': 'Waslost',
        'phone_number': 8139876543,
        'email': 'trentw@gmail.com'
    }
    contact3 = {
        'first_name': 'Tasha',
        'last_name': 'Rightpath',
        'phone_number': 8133217654,
        'email': 'tashar@gmail.com'
    }

    contacts = [contact1, contact2, contact3]

    for contact in contacts:
        first = contact['first_name']
        last = contact['last_name']
        phone = contact['phone_number']
        email = contact['email']
        c = add_contact(first, last, phone, email)

    for c in Contact.objects.all():
        print('- {0} - {1} - {2}'.format(c.full_name,
                                         c.phone_number,
                                         c.email))

def add_contact(first, last, phone, email):
    c = Contact.objects.get_or_create(phone_number=phone, email=email)[0]
    c.first_name = first
    c.last_name = last
    c.full_name = '{0}{1}{2}'.format(first, ' ', last)
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Contacts population script...')
    populate()
