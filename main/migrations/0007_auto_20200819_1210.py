# Generated by Django 3.1 on 2020-08-19 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200819_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.typepage', verbose_name='Категорія'),
        ),
    ]
