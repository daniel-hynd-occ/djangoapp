from django import forms
from django.forms import widgets
from django.forms.widgets import DateInput, Textarea, CheckboxInput, TextInput, FileInput

from .models import Project, VariableExtraction, VariableSet

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = [ 
            'date_created',
            'database_builder_state'
        ]
        widgets = {
            'isac_protocol': TextInput(attrs={'pattern': '\d{2}_\d{6}', 'title': 'ISAC protocol should have the pattern NN_NNNNNN, where N is a digit'}),
            'isac_approved': CheckboxInput(attrs={'onchange': 'isacApprovedChanged(this)'}),
            'protocol_title': Textarea(attrs={'rows': '3', 'class': 'project-create-isac-protocol'})
        }
        labels = {
            'isac_protocol': 'ISAC Protocol',
            'isac_approved': 'ISAC approved',
            'name': 'Abbreviated title'
        }

    field_order = ['isac_protocol', 'protocol_title', 'name', 'isac_approved']
        
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
