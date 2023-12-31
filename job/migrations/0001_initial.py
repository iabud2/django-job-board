# Generated by Django 5.0 on 2024-01-03 06:35

import django.db.models.deletion
import job.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=20)),
                ('description', models.TextField(max_length=1000)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('vacancy', models.IntegerField(default=1)),
                ('salary', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to=job.models.image_upload)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.category')),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=50)),
                ('website', models.URLField(max_length=100)),
                ('cv', models.FileField(upload_to='apply/')),
                ('coverletter', models.TextField(max_length=1500)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='job.job')),
            ],
        ),
    ]
