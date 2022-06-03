# Generated by Django 4.0.4 on 2022-06-03 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=256)),
                ('drink_category', models.CharField(max_length=256)),
                ('nutrition', models.CharField(max_length=256)),
                ('allergy', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'drink',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=256)),
                ('category_drinks', models.ManyToManyField(to='product.drink')),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]