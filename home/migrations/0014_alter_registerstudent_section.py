# Generated by Django 4.2.5 on 2023-10-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_registerstudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerstudent',
            name='section',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1, null=True),
        ),
    ]
