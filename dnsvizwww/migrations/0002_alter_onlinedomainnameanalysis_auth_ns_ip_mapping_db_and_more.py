# Generated by Django 4.0.5 on 2022-06-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsvizwww', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinedomainnameanalysis',
            name='auth_ns_ip_mapping_db',
            field=models.ManyToManyField(related_name='s+', to='dnsvizwww.nsmapping'),
        ),
        migrations.AlterField(
            model_name='onlinedomainnameanalysis',
            name='auth_ns_negative_response_db',
            field=models.ManyToManyField(related_name='s+', to='dnsvizwww.nsnamenegativeresponse'),
        ),
    ]
