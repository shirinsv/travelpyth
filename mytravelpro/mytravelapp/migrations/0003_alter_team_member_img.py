# Generated by Django 3.2.16 on 2023-01-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytravelapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='member_img',
            field=models.ImageField(upload_to='team_pics'),
        ),
    ]
