# Generated by Django 3.0.8 on 2020-07-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_certificate_certificade_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='training_date',
        ),
        migrations.AddField(
            model_name='certificate',
            name='finished_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='started_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='image',
            field=models.FileField(upload_to='certificate_images', verbose_name='Image'),
        ),
    ]
