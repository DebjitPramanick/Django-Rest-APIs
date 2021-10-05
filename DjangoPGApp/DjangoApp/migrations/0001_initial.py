# Generated by Django 3.2 on 2021-10-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ItemId', models.AutoField(primary_key=True, serialize=False)),
                ('ShopId', models.IntegerField()),
                ('ItemName', models.CharField(max_length=60)),
                ('ItemDescription', models.CharField(max_length=500)),
                ('ItemPrice', models.IntegerField()),
                ('ItemStock', models.IntegerField()),
                ('ItemType', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('ShopId', models.AutoField(primary_key=True, serialize=False)),
                ('ShopName', models.CharField(max_length=20)),
                ('ShopOwner', models.CharField(max_length=20)),
                ('ShopDescription', models.CharField(max_length=500)),
                ('ShopLocation', models.CharField(max_length=20)),
                ('ShopType', models.CharField(max_length=10)),
            ],
        ),
    ]
