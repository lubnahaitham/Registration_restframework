# Generated by Django 3.2.9 on 2022-01-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='seller',
        ),
        migrations.AddField(
            model_name='products',
            name='seller',
            field=models.ManyToManyField(to='rest.Seller'),
        ),
    ]
