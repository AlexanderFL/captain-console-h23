# Generated by Django 3.0.6 on 2020-05-05 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200505_2231'),
        ('store', '0003_auto_20200505_2231'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='UserPhotos',
        ),
        migrations.AddField(
            model_name='userphoto',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User'),
        ),
    ]
