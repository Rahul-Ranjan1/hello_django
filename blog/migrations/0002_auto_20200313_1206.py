# Generated by Django 2.1.3 on 2020-03-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat',
            field=models.CharField(max_length=1048576),
        ),
    ]