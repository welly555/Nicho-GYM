from django import forms
from gym.models import Aluno

from .utils import add_placeholder

class AlunoRegister(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'Nome',
            'sobrenome',
            'E_mail',
            'Data_Nascimento',
            'Valor_pagamento',
            'Situacao',
            'telefone',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['Nome'], 'Ex.: João')
        add_placeholder(self.fields['sobrenome'], 'Ex.: Almeida')
        add_placeholder(self.fields['E_mail'], 'Ex.: João@.com')
        add_placeholder(self.fields['Data_Nascimento'], 'Ex.: 10/10/2010')
        add_placeholder(self.fields['Valor_pagamento'], 'Ex.: 100')
        add_placeholder(self.fields['telefone'], '(00) 00000-0000')
        self.fields['Data_Nascimento'].widget.attrs.update({'class': 'mask-date'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        self.fields['Valor_pagamento'].widget.attrs.update({'class': 'mask-money'})
    
    Nome = forms.CharField(
        label='Nome do aluno:',
    )

    sobrenome = forms.CharField(
        label='Sobrenome:',
    )

    E_mail = forms.EmailField(
        label='E-mail:',
    )

    Data_Nascimento = forms.DateField(
        label='Data de Nascimento:',
    )

    Valor_pagamento = forms.CharField(
        label='Valor do Pagamento:',
    )

    Situacao = forms.BooleanField(
        label='Pagamento Realizado:',
    )

    telefone = forms.CharField(
        label='Telefone:',
    )