# Generated by Django 2.1.2 on 2018-10-27 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_venue_event_meetup_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='event_meetup_id',
            new_name='venue_meetup_id',
        ),
        migrations.AddField(
            model_name='event',
            name='event_meetup_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='venue',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]