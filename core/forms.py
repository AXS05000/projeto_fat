from django import forms
from django.core.exceptions import ValidationError
from django.core.mail.message import EmailMessage

from .models import BaseCNPJ, Notas


class NotasModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = Notas
        fields = ['baseinfocontratos', 'cnpj_da_nota', 'competencia_nota', 'tipo_de_faturamento', 'porcentagem_ans','competencia_nota_ans', 'quantidade_hora','baseinfocontratos2', 'quantidade_hora2','baseinfocontratos3', 'quantidade_hora3','baseinfocontratos4', 'quantidade_hora4','baseinfocontratos5', 'quantidade_hora5','baseinfocontratos6', 'quantidade_hora6','baseinfocontratos7', 'quantidade_hora7','baseinfocontratos8', 'quantidade_hora8','texto_livre','total_valor_outros']
        required = ['competencia_nota', 'tipo_de_faturamento', 'cnpj_da_nota']
        error_messages = {
            'porcentagem_ans': {
                'max_digits': 'Certifique-se de que tenha digitado o valor correto de porcentagem na ANS'
            }
        }



class BaseCNPJModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = BaseCNPJ
        fields = ['cnpj', 'nome_cliente', 'unidade', 'razao','avenida_rua', 'endereco','numero', 'complemento','bairro', 'municipio','uf', 'cep', 'iss', 'tipo_de_servico']
        required = ['cnpj', 'nome_cliente', 'unidade', 'razao','avenida_rua', 'endereco','numero','bairro', 'municipio','uf', 'cep', 'iss', 'tipo_de_servico']
