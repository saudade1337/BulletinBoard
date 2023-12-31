# Generated by Django 5.0 on 2023-12-11 17:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('TN', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('MC', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('BS', 'Кузнецы'), ('LW', 'Кожевники'), ('PM', 'Зельевары'), ('SM', 'Мастера заклинаний')], max_length=2)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('upload', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.advertisement')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
