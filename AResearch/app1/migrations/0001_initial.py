# Generated by Django 5.1.3 on 2024-11-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='')),
                ('psw', models.TextField(default='')),
                ('otp', models.TextField(default='')),
                ('email', models.TextField(default='')),
            ],
        ),
    ]
