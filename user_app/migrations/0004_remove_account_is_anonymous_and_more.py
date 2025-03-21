# Generated by Django 4.2.18 on 2025-03-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_account_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_anonymous',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_authenticated',
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
