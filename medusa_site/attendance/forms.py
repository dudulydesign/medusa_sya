from django import forms


class ApplyOvertimeForm(forms.Form):
  department = forms.ChoiceField(choices=[(0, ''),(1, 'IT'),(2, 'HR')])
  start_time = forms.DateTimeField()
  end_time = forms.DateTimeField()
  reason = forms.CharField(widget= forms.Textarea)


class OvertimeAuditForm(forms.Form):

  status = forms.ChoiceField(choices=[(1, 'OK'), (0, 'NO')])
  #reason = forms.CharField()

