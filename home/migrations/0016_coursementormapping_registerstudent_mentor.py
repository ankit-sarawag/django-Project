# Generated by Django 4.2.5 on 2023-10-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_registerstudent_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMentorMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=70, unique=True)),
                ('mentor', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='mentor',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]