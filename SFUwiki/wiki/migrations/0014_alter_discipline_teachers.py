# Generated by Django 4.2.5 on 2023-10-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0013_alter_discipline_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='disciplines', to='wiki.teacher'),
        ),
    ]
