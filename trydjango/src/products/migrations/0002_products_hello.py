# Generated by Django 2.0.7 on 2023-10-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='hello',
            field=models.TextField(default='this is great'),
        ),
    ]
