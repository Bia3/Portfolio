from django.contrib import admin
from .models import ContactCard, Bio, Address, GitHub, Keybase,\
    Codewars, LinkedIn, HackTheBox, CodePen


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


@admin.register(GitHub)
class GithubAdmin(admin.ModelAdmin):
    """"""

    list_display = ('view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return obj.contact_card.user.username


@admin.register(Keybase)
class KeybaseAdmin(admin.ModelAdmin):
    """"""

    list_display = ('view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return obj.contact_card.user.username


@admin.register(Codewars)
class CodewarsAdmin(admin.ModelAdmin):
    """"""

    list_display = ('view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return obj.contact_card.user.username


@admin.register(LinkedIn)
class LinkedInAdmin(admin.ModelAdmin):
    """"""

    list_display = ('view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return obj.contact_card.user.username


@admin.register(HackTheBox)
class HackTheBoxAdmin(admin.ModelAdmin):
    """"""

    list_display = ('view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return obj.contact_card.user.username


@admin.register(CodePen)
class CodePenAdmin(admin.ModelAdmin):
    """"""

    list_display = ('view_username', 'id')

    @staticmethod
    @admin.display(description='username')
    def view_username(obj):
        return obj.contact_card.user.username
