# Generated by Django 4.2.7 on 2023-12-27 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThreadStyle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menoversizedtshirt',
            name='available_sizes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='menoversizedtshirt',
            name='color',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mentshirt',
            name='available_sizes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mentshirt',
            name='color',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='womenoversizedtshirt',
            name='available_sizes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='womenoversizedtshirt',
            name='color',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='womentshirt',
            name='available_sizes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='womentshirt',
            name='color',
            field=models.TextField(),
        ),
    ]
