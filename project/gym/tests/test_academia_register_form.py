from django.test import TestCase
from django.urls import reverse
from gym.forms import RegisterForm
from parameterized import parameterized


class AcademiaRegisterFrom(TestCase):
    @parameterized.expand([
        ('Nome_academia', 'Ex.: fitnes gym'),
        ('Dono', 'Ex.: João Almaida'),
        ('E_mail', 'Ex.: João@.com'),
        ('telefone', '(00) 00000-0000'),
        ('cnpj', '00.000.00/0000.00'),
        ('Endereco', 'Ex.: Rua sem nome'),
        ('senha', 'senha'),
        ('confirma_senha', 'confirmar senha'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        test_placaholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(test_placaholder, placeholder)

    @parameterized.expand([
        ('Nome_academia', 'Nome da academia:'),
        ('Dono', 'Responsavel:'),
        ('E_mail', 'E-mail:'),
        ('telefone', 'Telefone:'),
        ('cnpj', 'CNPJ:'),
        ('Endereco', 'Endereço:'),
        ('senha', 'Senha:'),
        ('confirma_senha', 'Confirmar senha:'),
    ])
    def test_field_label(self, field, label):
        form = RegisterForm()
        test_label = form[field].field.label
        self.assertEqual(test_label, label)
