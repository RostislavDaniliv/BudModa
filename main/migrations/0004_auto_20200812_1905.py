# Generated by Django 3.1 on 2020-08-12 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_page_url_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='title',
            new_name='title_m',
        ),
    ]
