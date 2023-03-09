import openpyxl

from .models import BaseCNPJ


def update_basecnpj_from_excel(file_path):
    # Abre a planilha desejada
    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook['Planilha1']

    # Armazena os dados da planilha em uma lista de dicionários
    rows = list(worksheet.values)
    headers = rows[0]
    basecnpj_data = [dict(zip(headers, row)) for row in rows[1:]]

    # Atualiza os objetos do modelo BaseCNPJ com base nos dados da planilha
    for data in basecnpj_data:
        basecnpj = BaseCNPJ.objects.get(id=data['ID'])
        basecnpj.tipo_de_cliente = data['Tipo de Cliente']
        basecnpj.save()