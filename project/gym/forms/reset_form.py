import re

from django import forms
from django.core.exceptions import ValidationError

from .utils import add_placeholder


def strong_password(senha):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z](?=.*[0-9]).{8,}$)')

    if not regex.match(senha):
        raise ValidationError(
            ('A senha tem que ter pelo menos '
             'uma letra minuscula, '
             'uma maiuscula, '
             'um numero, '
             'e ter no minimo 8 caracteres.'
             ),
            code='Invalid'
        )


class Recuperar_senha(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['Senha'], 'Digite sua nova senha')
        add_placeholder(self.fields['Confirmar_Senha'],
                        'Confirme a nova senha')

    Senha = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            'required': 'Password invalida'
        },
        validators=[strong_password],
        label='Senha:'
    )
    Confirmar_Senha = forms.CharField(
        # required=True,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password invalida'
        },
        label='Confirmar senha:'
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('senha')
        password_confirmed = cleaned_data.get('confirma_senha')

        if password != password_confirmed:
            raise ValidationError(
                {
                    'confirma_senha': 'senhas diferente'
                }
            )
