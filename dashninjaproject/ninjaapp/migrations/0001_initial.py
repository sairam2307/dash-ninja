# Generated by Django 2.2.17 on 2020-12-04 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
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
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Footer',
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
                'db_table': 'footer',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=90, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ninjaapp.Category')),
            ],
            options={
                'managed': True,
                'db_table': 'items',
            },
        ),
    ]