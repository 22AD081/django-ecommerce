# Generated by Django 5.0.2 on 2024-03-02 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_products_account_details_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]