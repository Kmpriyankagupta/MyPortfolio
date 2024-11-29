# Generated by Django 4.2.16 on 2024-11-29 18:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homepagedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('about_headline', models.CharField(max_length=200)),
                ('about_headline_description', models.CharField(max_length=400)),
                ('about_headline_description1', models.CharField(max_length=40)),
                ('text_array', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, null=True, size=None)),
                ('clients_heading', models.CharField(max_length=200)),
                ('clients_description', models.CharField(max_length=400)),
                ('clients_description1', models.CharField(max_length=40)),
                ('exerpertise', models.CharField(max_length=200)),
                ('exerpertise_description', models.CharField(max_length=400)),
                ('expse_type1_heading', models.CharField(max_length=200)),
                ('expse_type1_description', models.CharField(max_length=400)),
                ('expse_type2_heading', models.CharField(max_length=200)),
                ('expse_type2_description', models.CharField(max_length=400)),
                ('expse_type3_heading', models.CharField(max_length=200)),
                ('expse_type3_description', models.CharField(max_length=400)),
                ('expse_type4_heading', models.CharField(max_length=200)),
                ('expse_type4_description', models.CharField(max_length=400)),
            ],
        ),
    ]
