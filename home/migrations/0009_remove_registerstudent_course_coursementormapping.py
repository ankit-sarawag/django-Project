# Generated by Django 4.2.5 on 2023-10-17 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_registerstudent_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerstudent',
            name='course',
        ),
        migrations.CreateModel(
            name='CourseMentorMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=70, unique=True)),
                ('mentor', models.CharField(max_length=80)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='home.registerstudent')),
            ],
        ),
    ]
