from django.test import TestCase
from django.urls import reverse


class GymURLSTest(TestCase):
    def test_gym_home_url_acept(self):
        url = reverse('gym:home')
        self.assertEqual(url, '/')

    def test_gym_cadastro_url_acept(self):
        url = reverse('gym:cadastro')
        self.assertEqual(url, '/cadastro/')

    def test_gym_login_url_acept(self):
        url = reverse('gym:login')
        self.assertEqual(url, '/login/')

    def test_gym_recuperar_senha_url_acept(self):
        url = reverse('gym:recuperar_senha')
        self.assertEqual(url, '/login/reset_senha')
    
    def test_gym_aluno_url_acept(self):
        url = reverse('gym:cadastro_aluno')
        self.assertEqual(url, '/aluno/')
    
