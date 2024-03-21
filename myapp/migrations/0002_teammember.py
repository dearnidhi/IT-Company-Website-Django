# Generated by Django 5.0.2 on 2024-03-01 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team_images/')),
                ('twitter_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('linkedin_link', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Team Members',
            },
        ),
    ]