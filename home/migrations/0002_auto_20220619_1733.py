# Generated by Django 3.2.13 on 2022-06-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categ',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='categ',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
