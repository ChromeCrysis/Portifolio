# Generated by Django 2.2.1 on 2019-07-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20190704_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='celular',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
