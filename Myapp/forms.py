from django import forms
from .models import FibonanciMethod

class FiboniciForm(forms.Form):
    class Meta:
        model = FibonanciMethod
        fields = ('number','startTime','endTime','totalTime','FiboniciList','Fibonaci_output')

