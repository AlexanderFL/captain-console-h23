# Generated by Django 3.0.6 on 2020-05-05 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('copies_sold', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField()),
                ('description', models.CharField(max_length=1024)),
                ('developer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Developers')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Genres')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Products')),
            ],
        ),
    ]
