# Generated by Django 4.2.7 on 2023-12-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenOversizedTshirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offer_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('available_sizes', models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=10, null=True)),
                ('color', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('fit', models.CharField(choices=[('regular', 'Regular Fit'), ('slim', 'Slim Fit'), ('loose', 'Loose Fit')], max_length=10)),
                ('sleeve', models.CharField(choices=[('short', 'Short Sleeve'), ('long', 'Long Sleeve')], max_length=10)),
                ('wash', models.CharField(choices=[('machine', 'Machine Wash'), ('hand', 'Hand Wash')], max_length=10)),
                ('occasion', models.CharField(max_length=255)),
                ('neck_type', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenTshirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offer_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('available_sizes', models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=10, null=True)),
                ('color', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('fit', models.CharField(choices=[('regular', 'Regular Fit'), ('slim', 'Slim Fit'), ('loose', 'Loose Fit')], max_length=10)),
                ('sleeve', models.CharField(choices=[('short', 'Short Sleeve'), ('long', 'Long Sleeve')], max_length=10)),
                ('wash', models.CharField(choices=[('machine', 'Machine Wash'), ('hand', 'Hand Wash')], max_length=10)),
                ('occasion', models.CharField(max_length=255)),
                ('neck_type', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WomenOversizedTshirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offer_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('available_sizes', models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=10, null=True)),
                ('color', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('fit', models.CharField(choices=[('regular', 'Regular Fit'), ('slim', 'Slim Fit'), ('loose', 'Loose Fit')], max_length=10)),
                ('sleeve', models.CharField(choices=[('short', 'Short Sleeve'), ('long', 'Long Sleeve')], max_length=10)),
                ('wash', models.CharField(choices=[('machine', 'Machine Wash'), ('hand', 'Hand Wash')], max_length=10)),
                ('occasion', models.CharField(max_length=255)),
                ('neck_type', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WomenTshirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('offer_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('available_sizes', models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=10, null=True)),
                ('color', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('fit', models.CharField(choices=[('regular', 'Regular Fit'), ('slim', 'Slim Fit'), ('loose', 'Loose Fit')], max_length=10)),
                ('sleeve', models.CharField(choices=[('short', 'Short Sleeve'), ('long', 'Long Sleeve')], max_length=10)),
                ('wash', models.CharField(choices=[('machine', 'Machine Wash'), ('hand', 'Hand Wash')], max_length=10)),
                ('occasion', models.CharField(max_length=255)),
                ('neck_type', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
