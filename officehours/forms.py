from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Request


class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ['slots', 'type', 'zoom_url', 'description']
        widgets = {
            'slots': forms.CheckboxSelectMultiple,
            'type': forms.RadioSelect,
            'zoom_url': forms.URLInput,
            'description': forms.Textarea(attrs={'rows': 4})
        }
        labels = {
            'slots': _('Please select the times you are available at:'),
            'type': _('Please specify the type of request:'),
            'zoom_url': _('URL of your Zoom meeting:'),
            'description': _('Describe the issue you need help with at office hours:')
        }
