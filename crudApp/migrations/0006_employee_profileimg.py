# Generated by Django 4.2.3 on 2023-08-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0005_employee_checkbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profileImg',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
