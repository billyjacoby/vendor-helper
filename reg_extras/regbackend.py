from registration.backends.default.views import RegistrationView
from reg_extras.forms import UserProfileRegistrationForm
from reg_extras.models import UserProfile

from django.contrib.sites.shortcuts import get_current_site

from registration.models import RegistrationProfile
from registration import signals


# this rewrites the registration-redux register() to include the data from work_app.models.UserProfile
class MyRegistrationView(RegistrationView):
    form_class = UserProfileRegistrationForm


    def register(self, form):
        site = get_current_site(self.request)
        if hasattr(form, 'save'):
            new_user_instance = form.save()
        else:
            new_user_instance = (UserProfile.objects.create_user(**form.cleaned_data))

        new_user = RegistrationProfile.objects.create_inactive_user(
        new_user = new_user_instance,
        site=site,
        send_email = self.SEND_ACTIVATION_EMAIL,
        request=self.request
        )
        signals.user_registered.send(sender=self.__class__, user=new_user, request=self.request)

        return new_user
