# Generated by Django 3.1.3 on 2020-12-01 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20201201_2323'),
        ('choice', '0003_auto_20201201_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.closequestion'),
        ),
    ]
