# Generated by Django 2.2.1 on 2019-05-04 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20190504_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]