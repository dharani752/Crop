# Generated by Django 4.2.3 on 2023-07-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='john', max_length=50)),
                ('email', models.CharField(default='john@gmail.com', max_length=50)),
                ('password', models.CharField(default='john', max_length=50)),
                ('phone', models.CharField(default='john', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='meruva', max_length=50)),
                ('lname', models.CharField(default='meruva', max_length=50)),
                ('email', models.CharField(default='john@gmail.com', max_length=50)),
                ('password', models.CharField(default='john', max_length=50)),
                ('phone', models.CharField(default='john', max_length=50)),
            ],
        ),
    ]
