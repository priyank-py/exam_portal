# Generated by Django 3.0 on 2019-12-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='about',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='About you'),
        ),
    ]
