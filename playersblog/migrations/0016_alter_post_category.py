# Generated by Django 4.0.6 on 2022-08-23 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playersblog', '0015_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Food', max_length=255),
        ),
    ]