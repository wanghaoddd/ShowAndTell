# Generated by Django 3.2.16 on 2022-10-15 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OFA', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofaimage',
            name='name',
        ),
    ]
