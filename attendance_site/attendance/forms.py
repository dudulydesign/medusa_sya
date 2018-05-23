from django import forms

class ApplyOvertimeForm(forms.Form):
  start_time = forms.DateTimeField()
  end_time = forms.DateTimeField()
  reason = forms.CharField(widget= forms.Textarea)

