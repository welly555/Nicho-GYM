import re

from django import forms
from django.core.exceptions import ValidationError
from gym.models import Academia


def strong_password(senha):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z](?=.*[0-9]).{8,}$)')

    if not regex.match(senha):
        raise ValidationError(
            ('A senha tem que ter pelo menos'
             'uma letra minuscula, '
             'uma maiuscula, '
             'um numero, '
             'e ter no minimo 8 caracteres'
             ),
            code='invalid'
        )


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['Nome_da_academia'], 'Ex.: fitnes gym')
        add_placeholder(self.fields['Proprietario'], 'Ex.: João Almaida')
        add_placeholder(self.fields['email'], 'Ex.: João@.com')
        add_placeholder(self.fields['email_confirmar'], 'Ex.: João@.com')
        add_placeholder(self.fields['cnpj'], '00.000.00/0000.00')
        add_placeholder(self.fields['Endereco'], 'Ex.: Rua sem nome')
        add_placeholder(self.fields['senha'], 'senha')
        add_placeholder(self.fields['confirma_senha'], 'confirmar senha')

    Nome_da_Academia = forms.CharField(
        error_messages={'requered': 'Escreva o nome da sua academia'},
        required=True,
        label='Nome da academia',
    )

    Poprietario = forms.CharField(
        error_messages={'requered': 'Escreva o nome do(a) proprietario'},
        required=True,
        label='Responsavel'
    )

    email = forms.EmailField(
        error_messages={'required': 'E-mail necessario'},
        required=True,
        label='E-mail',
        help_text='o email tem que ser valido'
    )
    email_confirmar = forms.EmailField(
        error_messages={'required': 'E-mail necessario'},
        required=True,
        label='E-mail',
        help_text='o email tem que ser valido'
    )
    cnpj = forms.CharField(
        error_messages={'requered': 'precisa do cnpj ativo da empresa'},
        required=True,
        label='CNPJ'
    )
    endereco = forms.CharField(
        error_messages={'requered': 'Escreva o endereço da academia'},
        required=True,
        label='Academia'
    )
    senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password invalida'
        },
        help_text=(
            'A senha precisa ter pelo menos um letra maiuscula, um minuscula,'
            'um numero e um caracter especial.'
            'E precisa ter o minimo 8 caracteres'
        ),
        validators=[strong_password],
        label='Password'
    )
    confirma_senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Password invalida'
        },
        label='Password'
    )

    def clean_email(self):
        email = self.cleaned_data('email', '')
        exists = Academia.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'Utilize um email valido', code='invalid'
            )

        return email

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
        email = cleaned_data.get('email')
        email_confirmed = cleaned_data.get('email_confirmar')

        if email != email_confirmed:
            raise ValidationError(
                {
                    'email_confirmar': 'emails diferente'
                }
            )
