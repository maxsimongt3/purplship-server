# Generated by Django 3.1.6 on 2021-02-16 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20210125_2125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracking',
            options={'ordering': ['-created_at'], 'verbose_name': 'Tracking Status', 'verbose_name_plural': 'Tracking Statuses'},
        ),
        migrations.AddField(
            model_name='tracking',
            name='delivered',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('purchased', 'purchased'), ('shipped', 'shipped'), ('transit', 'transit'), ('delivered', 'delivered')], default='created', max_length=50),
        ),
    ]
