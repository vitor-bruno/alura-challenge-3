# Generated by Django 4.0.4 on 2022-04-18 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='arquivos/')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco_origem', models.CharField(max_length=30)),
                ('agencia_origem', models.CharField(max_length=10)),
                ('conta_origem', models.CharField(max_length=20)),
                ('banco_destino', models.CharField(max_length=30)),
                ('agencia_destino', models.CharField(max_length=10)),
                ('conta_destino', models.CharField(max_length=20)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_hora', models.DateTimeField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('arquivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.arquivo')),
            ],
            options={
                'ordering': ['-data_hora'],
            },
        ),
    ]
