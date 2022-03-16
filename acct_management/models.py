import uuid
from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
import secured_fields


class ContactCard(models.Model):
    """
    Model for a contact card that has a 
    one to one relationship with User.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=250)
    phone = secured_fields.EncryptedCharField(max_length=20)


class Bio(models.Model):
    """A paragraph about the User"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=250)
    copy = MarkdownxField(max_length=500)


class Address(models.Model):
    """A set of protected fields for downloaded versions of the CV and Resume"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contact_card = models.OneToOneField(ContactCard, on_delete=models.CASCADE)
    street_one = secured_fields.EncryptedCharField(max_length=250)
    street_two = secured_fields.EncryptedCharField(max_length=250)
    city = secured_fields.EncryptedCharField(max_length=180)
    state = secured_fields.EncryptedCharField(max_length=180)
    zip = secured_fields.EncryptedCharField(max_length=10)


class GitHub(models.Model):
    """GitHub profile information"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contact_card = models.ForeignKey(ContactCard, on_delete=models.CASCADE)
    username = models.CharField(max_length=180)
    link = models.CharField(max_length=250)


class Keybase(models.Model):
    """Keybase profile information"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contact_card = models.ForeignKey(ContactCard, on_delete=models.CASCADE)
    username = models.CharField(max_length=180)
    link = models.CharField(max_length=250)


class Codewars(models.Model):
    """Codewars profile information"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contact_card = models.ForeignKey(ContactCard, on_delete=models.CASCADE)
    username = models.CharField(max_length=180)
    link = models.CharField(max_length=250)


class LinkedIn(models.Model):
    """LinkedIn profile information"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contact_card = models.ForeignKey(ContactCard, on_delete=models.CASCADE)
    username = models.CharField(max_length=180)
    link = models.CharField(max_length=250)


class HackTheBox(models.Model):
    """HackTheBox profile information"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contact_card = models.ForeignKey(ContactCard, on_delete=models.CASCADE)
    username = models.CharField(max_length=180)
    link = models.CharField(max_length=250)


class CodePen(models.Model):
    """CodePen profile information"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    contact_card = models.ForeignKey(ContactCard, on_delete=models.CASCADE)
    username = models.CharField(max_length=180)
    link = models.CharField(max_length=250)
