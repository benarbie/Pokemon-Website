# Generated by Django 5.0.6 on 2024-06-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_alter_pokemon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='fourx',
            field=models.JSONField(default='[]'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='halfx',
            field=models.JSONField(default='[]'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='images',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='onex',
            field=models.JSONField(default='[]'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='twox',
            field=models.JSONField(default='[]'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='zerox',
            field=models.JSONField(default='[]'),
        ),
    ]