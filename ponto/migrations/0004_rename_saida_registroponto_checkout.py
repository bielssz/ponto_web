# Generated by Django 5.1.3 on 2024-11-20 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0003_rename_checkout_registroponto_saida_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registroponto',
            old_name='saida',
            new_name='checkout',
        ),
    ]