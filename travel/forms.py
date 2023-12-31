from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'required':'',
            'name':'first_name',
            'type':'text',
            'class':'input',
        })
        self.fields["last_name"].widget.attrs.update({
            'required':'',
            'name':'last_name',
            'type':'text',
            'class':'input',
        })
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name':'username',
            'type':'text',
            'class':'input',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name':'email',
            'type':'email',
            'class':'input',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name':'password1',
            'type':'password',
            'class':'input',
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'name':'password2',
            'type':'password',
            'class':'input',
        })
    class Meta:
        model = User
        fields = ['first_name','username','password1','last_name','email','password2']
    
class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']

