# Generated by Django 5.1.3 on 2024-11-20 17:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0004_rename_saida_registroponto_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroponto',
            name='checkout',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
