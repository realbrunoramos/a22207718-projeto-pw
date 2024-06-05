# Generated by Django 4.0.6 on 2024-04-23 23:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='artigo',
            name='autorName',
        ),
        migrations.RemoveField(
            model_name='artigo',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='artigo',
            name='post',
        ),
        migrations.RemoveField(
            model_name='artigo',
            name='rating',
        ),
        migrations.AddField(
            model_name='artigo',
            name='autor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='conteudo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='data_publicacao',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='artigo',
            name='titulo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artigos.categoria'),
        ),
    ]
