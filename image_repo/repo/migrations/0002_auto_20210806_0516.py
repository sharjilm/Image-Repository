# Generated by Django 3.2.3 on 2021-08-06 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('action', models.CharField(choices=[('uploaded', 'uploaded'), ('deleted', 'deleted')], max_length=8)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('imageName', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', models.CharField(blank=True, max_length=500, null=True)),
                ('vision_tags', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('archived', models.BooleanField(default=False)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
