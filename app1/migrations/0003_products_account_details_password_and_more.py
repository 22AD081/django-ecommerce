# Generated by Django 5.0.2 on 2024-03-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_account_details_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('desc', models.CharField(max_length=30, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='account_details',
            name='password',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='account_details',
            name='phoneno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='account_details',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='account_details',
            name='firstname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account_details',
            name='lastname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
