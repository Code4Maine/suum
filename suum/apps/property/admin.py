from django.contrib import admin

from .models import Property, Owner, Assessment, MailingAddress, Building, Sale

admin.site.register(Building)
admin.site.register(Property)
admin.site.register(Owner)
admin.site.register(Assessment)
admin.site.register(MailingAddress)
admin.site.register(Sale)
