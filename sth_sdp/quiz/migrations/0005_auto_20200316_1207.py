# Generated by Django 2.2.7 on 2020-03-16 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20200303_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='q_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='question time to be alloted'),
        ),
        migrations.AddField(
            model_name='sitting',
            name='q_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='question time alloted'),
        ),
    ]