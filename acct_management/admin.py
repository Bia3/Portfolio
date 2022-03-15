from django.contrib import admin
from .models import ContactCard, Bio, Address


@admin.register(ContactCard)
class ContactCardAdmin(admin.ModelAdmin):
    """"""

    list_display = ('id', )


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    """"""

    list_display = ('profession', 'id')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """"""

    list_display = ('id', )
