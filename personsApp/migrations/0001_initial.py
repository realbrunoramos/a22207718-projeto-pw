# Generated by Django 4.0.6 on 2024-03-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('dateOfBirth', models.DateField()),
            ],
        ),
    ]