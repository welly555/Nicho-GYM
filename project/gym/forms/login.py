from django import forms


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['E_mail'], 'Seu email')
        add_placeholder(self.fields['Senha'], 'digite sua senha')

    E_mail = forms.EmailField()
    Senha = forms.CharField(
        widget=forms.PasswordInput()
    )
