# Generated by Django 5.0.2 on 2024-03-02 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_accessory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('desc', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]