# Generated by Django 5.0.4 on 2024-06-13 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.URLField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('sellername', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('adoptionfee', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(default='male', max_length=10)),
                ('size', models.CharField(default='small', max_length=10)),
                ('color', models.CharField(default='black', max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('spayed', models.CharField(default='no', max_length=10)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adoption.adoptionimage')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoption.seller')),
            ],
        ),
    ]
