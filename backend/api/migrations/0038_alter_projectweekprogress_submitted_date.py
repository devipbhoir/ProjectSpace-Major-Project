# Generated by Django 5.1.4 on 2025-04-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_alter_week_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectweekprogress',
            name='submitted_date',
            field=models.DateTimeField(),
        ),
    ]
