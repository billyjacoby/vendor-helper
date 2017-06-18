from django import forms
from website.models import TaskModel
from datetime import date

class TaskModelForm(forms.ModelForm):
    name = forms.CharField(required=True)
    location = forms.CharField(required=False)
    due_date = forms.DateField(widget=forms.SelectDateWidget, required=True, initial=date.today())
    description = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = TaskModel
        widgets = {
        'due_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = ('name', 'location', 'due_date', 'description')
