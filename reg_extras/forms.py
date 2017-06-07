from django import forms
from django.contrib.auth.models import User

from registration.forms import RegistrationForm

# this is what adds the new desired fields into the user class, be sure to fill out meta!
class UserProfileRegistrationForm(RegistrationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    company_name = forms.CharField()
#    reyes_email = forms.BooleanField()

#    def check_email(self):
#        email_domain = self['email'].split('@')
#        if 'reyesholdings.com' in email_domain:
#            self.reyes_email = True

    class Meta:
        model = User
        fields =('first_name', 'last_name', 'company_name', 'username', 'email', 'password1', 'password2')
