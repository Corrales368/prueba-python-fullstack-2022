# Import django
from django import forms


class BaseModelForm(forms.ModelForm):
    """
    Base class for inheritance with class css bootstrap
    """
    def __init__(self, *args, **kwargs):
        """
        Override method init for add class css bootstrap to forms
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})