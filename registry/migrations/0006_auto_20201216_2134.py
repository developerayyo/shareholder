# Generated by Django 3.1.4 on 2020-12-16 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0005_auto_20201216_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareholder',
            name='date_applied',
            field=models.DateField(blank=True, null=True),
        ),
    ]
