from django import forms

from users.models import UserModel


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
