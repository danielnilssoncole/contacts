from django import forms
from contacts.models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128,
                                 help_text='First Name: ')
    last_name = forms.CharField(max_length=128,
                                 help_text='Last Name: ')
    full_name = forms.CharField(widget=forms.HiddenInput(), required=False)
    phone_number = forms.IntegerField(max_value=9999999999,
                                      min_value=1000000000,
                                      help_text='Phone Number: ')
    email = forms.EmailField(max_length=254,
                             help_text='Email: ')
    created_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    updated_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone_number', 'email',)
