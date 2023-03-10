# Generated by Django 4.1.5 on 2023-01-20 17:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorId', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('kvk', models.CharField(max_length=100)),
                ('jobCategory', models.CharField(max_length=100)),
                ('userType', models.CharField(max_length=100)),
                ('premium', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('journey', models.CharField(max_length=100)),
                ('modality', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('subCategories', models.CharField(default='None', max_length=100)),
                ('salary', models.IntegerField()),
                ('salaryMin', models.IntegerField()),
                ('salaryMax', models.IntegerField()),
                ('salaryFreq', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('requirement', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('authorId', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]
