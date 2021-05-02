# Generated by Django 3.0.8 on 2021-05-01 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=50)),
                ('rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_number', models.IntegerField()),
                ('Beds', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('description', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to='room_image')),
                ('Capacity', models.IntegerField()),
                ('Category', models.ForeignKey(blank=True, null=True,
                                               on_delete=django.db.models.deletion.CASCADE, to='hotel_management_system.RoomCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('room', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='hotel_management_system.Room')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
