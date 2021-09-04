from django import forms
from .models import Question,Choice
 
class MyForma(forms.ModelForm):
  class Meta:
    model = Question
    fields = '__all__'

class MyFormb(forms.ModelForm):
  class Meta:
    model = Choice
    fields = ['question','choice_text']
