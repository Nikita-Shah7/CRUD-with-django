# Generated by Django 4.2.3 on 2023-08-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
    ]
