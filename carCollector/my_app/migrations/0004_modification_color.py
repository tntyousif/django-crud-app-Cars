# Generated by Django 5.1.3 on 2024-12-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_filling_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='modification',
            name='color',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
