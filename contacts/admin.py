from django.contrib import admin
from contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', )

admin.site.register(Contact, ContactAdmin)
