# Generated by Django 3.0.6 on 2020-05-05 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=200)),
                ('alt', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='userphotos',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='paymentinfo',
            name='cvc',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
