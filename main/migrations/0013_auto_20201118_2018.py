# Generated by Django 3.1 on 2020-11-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201118_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='on_fav',
            field=models.BooleanField(default=False, verbose_name='На головну'),
        ),
        migrations.DeleteModel(
            name='Fav_page',
        ),
    ]