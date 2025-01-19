from django import forms
from .models import PetOwner, Pet

class OwnerForm(forms.ModelForm):
    class Meta:
        model = PetOwner
        fields = ("first_name", "last_name", "address", "email", "phone")


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet 
        fields = ("name", "owner",)
