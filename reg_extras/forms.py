from django import forms
from django.contrib.auth.models import User
from django import forms
from registration.forms import RegistrationForm
from django.contrib.auth.forms import UserChangeForm

from .models import UserProfile

#for password replacement
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField

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

class PasswordFieldEdit(ReadOnlyPasswordHashField):
    pass


class EditUserProfileForm(forms.ModelForm):
    """
    This class is a carbon copy of the UserChangeForm class from
    django.contrib.auth.forms, with the password functionality deleted, and
    the form is modified to allow changes to be made to the
    UserProfle, which extends the Django User
    """
    class Meta:
        model = UserProfile
        fields = ('company_name',)

    def __init__(self, *args, **kwargs):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')
