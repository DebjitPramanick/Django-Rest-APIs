# Generated by Django 3.2 on 2021-10-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('listID', models.AutoField(primary_key=True, serialize=False)),
                ('listName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskID', models.AutoField(primary_key=True, serialize=False)),
                ('taskName', models.CharField(max_length=50)),
                ('taskStatus', models.BooleanField(default=False)),
                ('listId', models.IntegerField()),
            ],
        ),
    ]