# Generated by Django 2.2.4 on 2020-02-12 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atebweb', '0006_videogaleria'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='categoria',
            field=models.ForeignKey(default=30, on_delete=django.db.models.deletion.PROTECT, to='atebweb.Categoria'),
            preserve_default=False,
        ),
    ]