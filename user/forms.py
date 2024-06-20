from django import forms
from user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email','image']

    def save(self, commit=False):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user







class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image','video', 'username', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super(ProfileUpdateForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.username = self.cleaned_data['username']
        user.image = self.cleaned_data['image']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user