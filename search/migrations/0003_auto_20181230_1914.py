# Generated by Django 2.1.4 on 2018-12-30 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20181230_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thesis',
            options={'ordering': ('-publish',), 'verbose_name_plural': 'Theses'},
        ),
    ]