# Generated by Django 4.0.4 on 2022-04-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_name_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
