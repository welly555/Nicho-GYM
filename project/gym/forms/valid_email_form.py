from django import forms

from .utils import add_placeholder


class Valid_Email(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['email'], 'Ex.: João@.com')

    email = forms.EmailField(
        error_messages={'required': 'E-mail necessario'},
        required=True,
        label='E-mail:',
    )
