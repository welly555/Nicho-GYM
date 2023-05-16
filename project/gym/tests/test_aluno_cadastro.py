from django.test import TestCase
from django.urls import reverse
from gym.forms import AlunoRegister
from parameterized import parameterized


class AlunoRegisterForm(TestCase):
    @parameterized.expand([
        ('Nome', 'Ex.: João'),
        ('sobrenome', 'Ex.: Almeida'),
        ('E_mail', 'Ex.: João@.com'),
        ('Data_Nascimento', 'Ex.: 10/10/2010'),
        ('Valor_pagamento', 'Ex.: 100'),
        ('telefone', '(00) 00000-0000'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = AlunoRegister()
        test_placaholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(test_placaholder, placeholder)

    @parameterized.expand([
        ('Nome', 'Nome do aluno:'),
        ('sobrenome', 'Sobrenome:'),
        ('E_mail', 'E-mail:'),
        ('Data_Nascimento', 'Data de Nascimento:'),
        ('Valor_pagamento', 'Valor do Pagamento:'),
        ('telefone', 'Telefone:'),
    ])
    def test_field_label(self, field, label):
        form = AlunoRegister()
        test_label = form[field].field.label
        self.assertEqual(test_label, label)
