# Generated by Django 3.2.9 on 2021-11-08 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_post_head_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='head_image',
            new_name='upload_image',
        ),
    ]
