# Generated by Django 3.2.16 on 2023-01-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_remove_registereduser_confirm_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignInUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
