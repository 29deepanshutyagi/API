# Generated by Django 4.2.7 on 2023-11-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('units', models.CharField(max_length=50)),
                ('end_date', models.DateField()),
                ('value', models.IntegerField()),
                ('accn', models.TextField()),
                ('fiscal_year', models.IntegerField()),
                ('filing_form', models.CharField(max_length=20)),
                ('filed_date', models.DateField()),
                ('frame', models.TextField()),
            ],
        ),
    ]
