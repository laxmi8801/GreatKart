# Generated by Django 3.1 on 2022-01-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_variation'),
        ('cartes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='Store.Variation'),
        ),
    ]
