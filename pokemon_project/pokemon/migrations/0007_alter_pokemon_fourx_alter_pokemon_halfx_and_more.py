# Generated by Django 5.0.6 on 2024-06-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0006_alter_pokemon_fourx_alter_pokemon_halfx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='fourx',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='halfx',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='onex',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='twox',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='zerox',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
