# Generated by Django 3.1 on 2020-08-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200812_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title_page',
            field=models.CharField(default='BudModa', max_length=50, verbose_name='Title (seo) сторінки'),
        ),
    ]
