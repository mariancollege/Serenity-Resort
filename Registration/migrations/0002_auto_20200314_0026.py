# Generated by Django 3.0.2 on 2020-03-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='type',
            field=models.CharField(default='user', max_length=50),
        ),
    ]
