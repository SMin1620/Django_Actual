# Generated by Django 3.2.1 on 2021-05-12 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stuck',
            new_name='stock',
        ),
    ]