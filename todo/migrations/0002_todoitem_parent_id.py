# Generated by Django 2.2.1 on 2019-05-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='parent_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]