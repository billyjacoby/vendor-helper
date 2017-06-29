from django import forms
from website.models import TaskModel, UserIncentiveModel
from datetime import date

class TaskModelForm(forms.ModelForm):
    name = forms.CharField(required=True)
    location = forms.CharField(required=False)
    due_date = forms.DateField(widget=forms.SelectDateWidget, required=True, initial=date.today())
    description = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = TaskModel
        widgets = {
        'payout': forms.NumberInput(),
        'due_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = ('name', 'location', 'due_date', 'description')

class UserIncentiveModelForm(forms.ModelForm):
    date_completed = forms.DateField(widget=forms.SelectDateWidget, initial=date.today())
    class Meta:
        model = UserIncentiveModel
        widgets = {
        'date_completed': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = (
        'payout',
        'location',
        'comments',
        'completed',
        'payed',
        'date_completed',
        )
