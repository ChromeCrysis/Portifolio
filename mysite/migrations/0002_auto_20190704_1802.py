# Generated by Django 2.2.1 on 2019-07-04 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='celular',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
