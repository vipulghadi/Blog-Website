# Generated by Django 4.2.5 on 2023-09-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_blogpost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_on',
            field=models.DateField(auto_now=True),
        ),
    ]
