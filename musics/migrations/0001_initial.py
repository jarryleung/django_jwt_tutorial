# Generated by Django 2.1.7 on 2019-02-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.TextField()),
                ('singer', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'music',
            },
        ),
    ]
