# Generated by Django 2.2.17 on 2020-12-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=90, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': True,
                'db_table': 'company',
            },
        ),
    ]
