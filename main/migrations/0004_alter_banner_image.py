# Generated by Django 3.2.9 on 2021-12-04 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
