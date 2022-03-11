import uuid
from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField


class ContactCard(models.Model):
    """
    Model for a contact card that has a one to many relationship with
    User.
    Posibly use https://django-fernet-fields.readthedocs.io/en/latest/ or
    https://pypi.org/project/django-encrypted-model-fields/ to encypt
    phone
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=250)
    # phone = models.CharField(max_length = 20)


class Bio(models.Model):
    """A paragraph about the User"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=250)
    copy = MarkdownxField(max_length=3000)


class Address(models.Model):
    """"""
    id = models.UUIDField(
        primar_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contact_card = models.ForeignKey(ContactCard, on_delete=models.CASCADE)
