# Generated by Django 2.2.4 on 2020-02-12 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atebweb', '0007_partido_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partido',
            name='categoria',
        ),
    ]
