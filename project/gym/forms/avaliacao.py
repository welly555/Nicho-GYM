from django import forms
from django.core.exceptions import ValidationError
from gym.models import Avaliacao

from .utils import add_placeholder


class AvalicaoRegister(forms.Form):
    class Meta:
        model = Avaliacao
        fields = [
            'peso',
            'altura',
            'Dobra_tripical',
            'Dobra_abdominal',
            'Dobra_subescapular',
            'Dobra_axilar_media ',
            'Dobra_coxa ',
            'Dobra_toracica ',
            'Dobra_suprailiaca ',
            'Circoferencia_pescoco ',
            'Circoferencia_torax ',
            'Circoferencia_ombro ',
            'Circoferencia_cintura ',
            'Circoferencia_quadril',
            'Circoferencia_abdomen',
            'Circoferencia_braco_relaxado',
            'Circoferencia_braco_contraido',
            'Circoferencia_antebraco',
            'Circoferencia_prox_coxa',
            'Circoferencia_medial_coxa',
            'Circoferencia_distal_coxa',
            'Circoferencia_panturilha_coxa',
        ]
    peso = forms.FloatField(required=False)
    altura = forms.FloatField(required=False)
    Dobra_tripical = forms.FloatField(required=False)
    Dobra_abdominal = forms.FloatField(required=False)
    Dobra_subescapular = forms.FloatField(required=False)
    Dobra_axilar_media = forms.FloatField(required=False)
    Dobra_coxa = forms.FloatField(required=False)
    Dobra_toracica = forms.FloatField(required=False)
    Dobra_suprailiaca = forms.FloatField(required=False)
    Circoferencia_pescoco = forms.FloatField(required=False)
    Circoferencia_torax = forms.FloatField(required=False)
    Circoferencia_ombro = forms.FloatField(required=False)
    Circoferencia_cintura = forms.FloatField(required=False)
    Circoferencia_quadril = forms.FloatField(required=False)
    Circoferencia_abdomen = forms.FloatField(required=False)
    Circoferencia_braco_relaxado = forms.FloatField(required=False)
    Circoferencia_braco_contraido = forms.FloatField(required=False)
    Circoferencia_antebraco = forms.FloatField(required=False)
    Circoferencia_prox_coxa = forms.FloatField(required=False)
    Circoferencia_medial_coxa = forms.FloatField(required=False)
    Circoferencia_distal_coxa = forms.FloatField(required=False)
    Circoferencia_panturilha_coxa = forms.FloatField(required=False)
