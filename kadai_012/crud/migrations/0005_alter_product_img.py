# Generated by Django 5.0.7 on 2024-07-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_rename_category_product_category_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='noImage.png', upload_to=''),
        ),
    ]
