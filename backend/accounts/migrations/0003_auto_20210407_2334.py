# Generated by Django 3.1.7 on 2021-04-07 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210407_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='E-mail Address'),
        ),
    ]
