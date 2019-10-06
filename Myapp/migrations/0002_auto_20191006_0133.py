# Generated by Django 2.1.1 on 2019-10-05 20:03

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fibonancimethod',
            name='Fibonaci_output',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fibonancimethod',
            name='FiboniciList',
            field=jsonfield.fields.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fibonancimethod',
            name='endTime',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fibonancimethod',
            name='startTime',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fibonancimethod',
            name='totalTime',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
