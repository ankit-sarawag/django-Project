# Generated by Django 4.2.5 on 2023-10-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_registerstudent_date_alter_registerstudent_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerstudent',
            name='firstname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='lastname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]