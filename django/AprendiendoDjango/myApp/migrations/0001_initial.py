# Generated by Django 5.0.4 on 2024-04-21 02:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('public', models.BooleanField()),
                ('dateCreate', models.DateTimeField(auto_now_add=True)),
                ('dateUpdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('dateCreate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
