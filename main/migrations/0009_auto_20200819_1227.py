# Generated by Django 3.1 on 2020-08-19 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200819_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='categories',
        ),
        migrations.AddField(
            model_name='page',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.typepage'),
        ),
    ]
