# Generated by Django 3.1.1 on 2021-03-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0007_auto_20210311_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='approve',
            field=models.CharField(default='p', max_length=2),
        ),
    ]
