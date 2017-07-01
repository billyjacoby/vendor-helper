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

class MonthForm(forms.Form):
    month_choices = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December")
    )
    month = forms.ChoiceField(choices=month_choices, label="", initial=date.today().month, widget=forms.Select() )

    class Meta:
        fields = ['month']
