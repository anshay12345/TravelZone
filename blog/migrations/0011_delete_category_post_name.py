# Generated by Django 4.0.4 on 2022-04-29 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='coding', max_length=20),
        ),
    ]
