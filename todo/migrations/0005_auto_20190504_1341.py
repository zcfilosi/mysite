# Generated by Django 2.2.1 on 2019-05-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20190504_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='parent_id',
            field=models.IntegerField(),
        ),
    ]
