# Generated by Django 4.2.5 on 2023-10-11 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0009_alter_department_logo_alter_discipline_teachers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='teachers',
            field=models.ManyToManyField(default=None, related_name='disciplines', to='wiki.teacher'),
        ),
    ]