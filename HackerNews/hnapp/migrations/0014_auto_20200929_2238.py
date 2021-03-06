# Generated by Django 3.1 on 2020-09-29 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hnapp', '0013_auto_20200929_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hnapp.comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='votes',
            field=models.IntegerField(null=True),
        ),
    ]
