# Generated by Django 4.0.2 on 2022-02-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employeedetail_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
