from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from gamer.models import Gamer

class RegistrationForm(ModelForm):
        username        = forms.CharField(label=(u'User Name'))
        email           = forms.EmailField(label=(u'Email Address'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        password1       = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

        class Meta:
                model = Gamer
                exclude = ('user',)

        def clean_username(self):
                username = self.cleaned_data['username']
                try:
                        User.objects.get(username=username)
                except User.DoesNotExist:
                        return username
                raise forms.ValidationError("Pick another name if you wanna game.")

        def clean(self):
                if self.cleaned_data['password'] != self.cleaned_data['password1']:
                        raise forms.ValidationError("The passwords did not match. CORRECT IT NOW!")
                return self.cleaned_data

class LoginForm(forms.Form):
        username        = forms.CharField(label=(u'User Name'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	
