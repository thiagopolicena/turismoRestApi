# Generated by Django 2.1.1 on 2018-09-01 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='longitudo',
            new_name='longitude',
        ),
    ]
