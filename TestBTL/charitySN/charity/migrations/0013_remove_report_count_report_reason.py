# Generated by Django 4.0.4 on 2022-05-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0012_auctionloser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='count',
        ),
        migrations.AddField(
            model_name='report',
            name='reason',
            field=models.TextField(null=True),
        ),
    ]
