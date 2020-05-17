from django.forms import ModelForm
from app.models import table

class formtable(ModelForm):
    class Meta:
        model = table
        fields = ['name', 'text']