# Generated by Django 4.0.4 on 2022-05-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0004_report_auctioninfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
