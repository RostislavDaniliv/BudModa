# Generated by Django 3.1 on 2020-08-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_page_title_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='categories',
        ),
        migrations.AddField(
            model_name='page',
            name='categories',
            field=models.CharField(default='', max_length=200, verbose_name='Назва категорії'),
        ),
    ]
