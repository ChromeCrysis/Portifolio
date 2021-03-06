# Generated by Django 2.2.1 on 2019-07-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id_contato', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('mensagem', models.TextField(blank=True, max_length=300, verbose_name='Mensagem')),
            ],
        ),
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id_atualizacao', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=35)),
                ('legenda', models.CharField(max_length=150)),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='mysite\\static\\img', verbose_name='Imagem')),
                ('atualizado_em', models.DateTimeField(auto_now_add=True, verbose_name='Atualizdo em ')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
    ]
