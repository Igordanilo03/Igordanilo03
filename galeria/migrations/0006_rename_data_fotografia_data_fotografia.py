# Generated by Django 5.1.1 on 2024-09-15 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='data',
            new_name='data_fotografia',
        ),
    ]
