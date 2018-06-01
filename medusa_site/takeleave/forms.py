from django import forms


class ApplyTakeleaveForm(forms.Form):
  category = forms.ChoiceField(choices=[(0, ''),(1, 'Leave for Statutory Reasons'),(2, 'Personal Leave'),(3, 'Menstrual Leave'),(4, 'Sick Leave')])
  department = forms.ChoiceField(choices=[(0, ''),(1, 'IT'),(2, 'HR')])
  start_time = forms.DateTimeField()
  end_time = forms.DateTimeField()
  reason = forms.CharField(widget = forms.Textarea)

class TakeleaveForm(forms.Form):
  status = forms.ChoiceField(choices=[(1, 'OK'),(0, 'NO')])
