# Generated by Django 4.2.3 on 2023-08-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0008_alter_employee_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profileImg',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
    ]
