# Generated by Django 3.0.5 on 2020-04-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passmjrapp', '0008_auto_20200418_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordaccount',
            name='additional_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]