# Generated by Django 5.0 on 2023-12-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThejsonCruderApp', '0009_alter_contact_confirm_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_data', models.JSONField()),
            ],
        ),
    ]