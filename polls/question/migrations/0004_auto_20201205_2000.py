# Generated by Django 3.1.3 on 2020-12-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20201205_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='number_of_choices',
            field=models.IntegerField(default=1),
        ),
    ]
