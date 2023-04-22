# Generated by Django 4.1.7 on 2023-04-22 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zaunita', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='nombre',
            new_name='user',
        ),
        migrations.AddField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='perfil'),
        ),
    ]