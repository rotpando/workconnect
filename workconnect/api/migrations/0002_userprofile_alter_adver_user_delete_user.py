# Generated by Django 4.1.5 on 2023-01-23 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('kvk', models.CharField(max_length=100)),
                ('jobCategory', models.CharField(max_length=100)),
                ('userType', models.CharField(max_length=100)),
                ('premium', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='adver',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]