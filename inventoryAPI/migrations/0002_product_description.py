# Generated by Django 4.2.1 on 2023-05-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='Description of the product'),
            preserve_default=False,
        ),
    ]
