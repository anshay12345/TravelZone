# Generated by Django 4.0.4 on 2022-04-29 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_category_post_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='category',
        ),
    ]
