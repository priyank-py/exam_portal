# Generated by Django 3.0 on 2019-12-17 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]