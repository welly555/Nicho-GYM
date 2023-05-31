from django import forms

from .utils import add_placeholder


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['Responsavel'], 'Nome do responsavel')
        add_placeholder(self.fields['Senha'], 'digite sua senha')

    Responsavel = forms.CharField()
    Senha = forms.CharField(
        widget=forms.PasswordInput()
    )
