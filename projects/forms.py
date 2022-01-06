from django import forms
from django.forms import widgets
from django.forms.widgets import DateInput, Textarea

from .models import Project, VariableExtraction, VariableSet

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = [ 
            'name', 
            'date_created'
        ]
        widgets = {
            'protocol_title': Textarea()
        }
        labels = {
            'isac_protocol': 'ISAC Protocol',
            'isac_approved': 'ISAC Approved'
        }

class VariableSetForm(forms.ModelForm):
    class Meta:
        exclude=['project']
        widgets= {
            'index_date': DateInput(attrs={'type':'date'})
        }
        model = VariableSet
        
class DatabaseBuilderForm(forms.Form):
    input_directory = forms.CharField()

class VariableExtractionForm(forms.ModelForm):
    class Meta:
        exclude = [
            'project',
            'state'
            ]
        model = VariableExtraction
