# Generated by Django 2.1.3 on 2020-03-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200313_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='chat',
            field=models.CharField(max_length=1048576),
        ),
    ]