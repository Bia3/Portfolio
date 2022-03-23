from django.contrib import admin
from .models import ContactCard, Bio, Address


@admin.register(ContactCard)
class ContactCardAdmin(admin.ModelAdmin):
    """Settings for the Contact Card model on the Admin page"""

    list_display = ('view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return obj.user.username


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    """Settings for the Bio model on the Admin page"""

    list_display = ('view_username', 'profession', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return obj.user.username


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Settings for the Address model on the Admin page"""

    list_display = ('view_username', 'street_one', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return obj.contact_card.user.username
