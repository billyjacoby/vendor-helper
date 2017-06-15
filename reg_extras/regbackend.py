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
        company_name = form.cleaned_data['company_name']
        company = form.cleaned_data['company']
        new_user = RegistrationProfile.objects.create_inactive_user(
        new_user = new_user_instance,
        site=site,
        send_email = self.SEND_ACTIVATION_EMAIL,
        request=self.request,
        )
        # the following two lines are necessary to add new fields to the user
        # profile upon registration
        new_profile = UserProfile.objects.create(user=new_user, company_name=company_name, company=company)
        new_profile.save()

        signals.user_registered.send(sender=self.__class__, user=new_user, request=self.request)
        return new_user
