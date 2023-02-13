from django import forms
from django.core.mail.message import EmailMessage

from .models import BaseCNPJ, Notas


class NotasModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Notas
        fields = ['baseinfocontratos', 'cnpj_da_nota', 'competencia_nota', 'tipo_de_faturamento', 'quantidade_hora','baseinfocontratos2', 'quantidade_hora2','baseinfocontratos3', 'quantidade_hora3','baseinfocontratos4', 'quantidade_hora4','baseinfocontratos5', 'quantidade_hora5','baseinfocontratos6', 'quantidade_hora6','baseinfocontratos7', 'quantidade_hora7','baseinfocontratos8', 'quantidade_hora8']
        required = ['baseinfocontratos','competencia_nota', 'tipo_de_faturamento', 'quantidade_hora', 'cnpj_da_nota']

class BaseCNPJModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = BaseCNPJ
        fields = ['cnpj', 'nome_cliente', 'unidade', 'razao','avenida_rua', 'endereco','numero', 'complemento','bairro', 'municipio','uf', 'cep', 'iss', 'tipo_de_servico']
        required = ['cnpj', 'nome_cliente', 'unidade', 'razao','avenida_rua', 'endereco','numero', 'complemento','bairro', 'municipio','uf', 'cep', 'iss', 'tipo_de_servico']
