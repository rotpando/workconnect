# Generated by Django 4.1.5 on 2023-01-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('companyName', models.TextField()),
                ('city', models.TextField()),
                ('journey', models.TextField()),
                ('modality', models.TextField()),
                ('category', models.TextField()),
                ('sub_categories', models.TextField()),
                ('salary', models.IntegerField()),
                ('salary_min', models.IntegerField()),
                ('salary_max', models.IntegerField()),
                ('salary_freq', models.IntegerField()),
                ('description', models.TextField()),
                ('requirement', models.TextField()),
                ('zip', models.TextField()),
                ('authorId', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
    ]