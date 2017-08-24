from django import forms
from contacts.models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128,
                                 help_text='First Name: ')
    last_name = forms.CharField(max_length=128,
                                 help_text='Last Name: ')
    full_name = forms.CharField(widget=forms.HiddenInput())
