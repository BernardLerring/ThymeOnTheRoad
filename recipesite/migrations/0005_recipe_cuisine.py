# Generated by Django 3.2.13 on 2022-06-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesite', '0004_auto_20220611_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cuisine',
            field=models.TextField(max_length=20, null=True, unique=True),
        ),
    ]
