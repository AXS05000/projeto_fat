# Generated by Django 4.1.5 on 2023-02-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_basecnpj_tipo_de_cliente_alter_notas_quantidade_hora_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='porcentagem_ans',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Porcentagem ANS'),
            preserve_default=False,
        ),
    ]
