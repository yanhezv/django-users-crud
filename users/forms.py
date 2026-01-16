from django import forms

from .models import User


class UserForm(forms.ModelForm):
    """
    Form for creating and updating users.
    """

    class Meta:
        model = User
        fields = ["username", "email", "is_active"]
