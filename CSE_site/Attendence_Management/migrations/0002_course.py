# Generated by Django 4.1 on 2023-04-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendence_Management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=2)),
                ('courses', models.TextField()),
                ('facultyHandles', models.TextField()),
            ],
        ),
    ]
