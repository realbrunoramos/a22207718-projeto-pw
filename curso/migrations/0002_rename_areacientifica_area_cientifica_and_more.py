# Generated by Django 4.0.6 on 2024-04-23 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AreaCientifica',
            new_name='area_Cientifica',
        ),
        migrations.DeleteModel(
            name='LinguagemProgramacao',
        ),
    ]