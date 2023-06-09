import re

from django import forms
from django.core.exceptions import ValidationError
from gym.models import Academia

from .utils import add_placeholder


def strong_password(senha):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z](?=.*[0-9]).{8,}$)')

    if not regex.match(senha):
        raise ValidationError(
            ('A senha tem que ter pelo menos'
             'uma letra minuscula, '
             'uma maiuscula, '
             'um numero, '
             'e ter no minimo 8 caracteres.'
             ),
            code='Invalid'
        )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Academia
        fields = [
            'Nome_academia',
            'username',
            'email',
            'telefone',
            'cnpj',
            'Endereco',
            'password',
            'confirma_senha'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['Nome_academia'], 'Ex.: fitnes gym')
        add_placeholder(self.fields['username'], 'Ex.: João Almaida')
        add_placeholder(self.fields['email'], 'Ex.: João@.com')
        add_placeholder(self.fields['telefone'], '(00) 00000-0000')
        add_placeholder(self.fields['cnpj'], '00.000.00/0000.00')
        add_placeholder(self.fields['Endereco'], 'Ex.: Rua sem nome')
        add_placeholder(self.fields['password'], 'senha')
        add_placeholder(self.fields['confirma_senha'], 'confirmar senha')
        self.fields['cnpj'].widget.attrs.update({'class': 'mask-cnpj'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})

    Nome_academia = forms.CharField(
        error_messages={'requered': 'Escreva o nome da sua academia'},
        required=True,
        label='Nome da academia:',
    )

    username = forms.CharField(
        error_messages={'requered': 'Escreva o nome do(a) proprietario'},
        required=True,
        label='Responsavel:'
    )

    email = forms.EmailField(
        error_messages={'required': 'E-mail necessario'},
        required=True,
        label='E-mail:',
    )
    telefone = forms.CharField(
        # validators=[phone],
        error_messages={
            'requerid': 'telefone invalido'
        },
        label='Telefone:',

    )
    cnpj = forms.CharField(
        error_messages={'requered': 'precisa do cnpj ativo da empresa'},
        required=True,
        label='CNPJ:'
    )
    Endereco = forms.CharField(
        error_messages={'requered': 'Escreva o endereço da academia'},
        required=True,
        label='Endereço:'
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password invalida'
        },
        # help_text=(
        #     'A senha precisa ter pelo menos uma letra maiuscula, uma minuscula,'  # noqa: E501
        #     'um numero e um caracter especial.'
        #     'E precisa ter o minimo 8 caracteres'
        # ),
        validators=[strong_password],
        label='Senha:'
    )
    confirma_senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password invalida'
        },
        # help_text=(
        #     'A senha precisa ter pelo menos uma letra maiuscula, uma minuscula,'  # noqa: E501
        #     'um numero e um caracter especial.'
        #     'E precisa ter o minimo 8 caracteres'
        # ),
        label='Confirmar senha:'

    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirmed = cleaned_data.get('confirma_senha')

        if password != password_confirmed:
            raise ValidationError(
                {
                    'confirma_senha': 'senhas diferente'
                }
            )

        email = cleaned_data.get('email')

        exists = Academia.objects.filter(email=email).exists()

        if exists:
            raise ValidationError({
                'email': 'email invalido'
            })
