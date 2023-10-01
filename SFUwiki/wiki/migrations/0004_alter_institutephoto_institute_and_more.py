# Generated by Django 4.2.5 on 2023-10-01 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_department_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutephoto',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='wiki.institute'),
        ),
        migrations.AlterField(
            model_name='teacherphoto',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='wiki.teacher'),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='discipline_photo')),
                ('teachers', models.ManyToManyField(related_name='disciplines', to='wiki.teacher')),
            ],
        ),
    ]
