# Generated by Django 5.0.2 on 2024-03-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_searchhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='desc',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
