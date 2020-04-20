# Generated by Django 3.0.4 on 2020-04-14 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('username', models.CharField(blank=True, max_length=45, null=True)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('additional_notes', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
