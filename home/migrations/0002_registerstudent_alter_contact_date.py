# Generated by Django 4.2.5 on 2023-10-15 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=10)),
                ('primaryEmail', models.EmailField(max_length=254)),
                ('alternateEmail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('rollno', models.IntegerField(max_length=5)),
                ('birthDate', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('course', models.CharField(max_length=70)),
                ('semester', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]