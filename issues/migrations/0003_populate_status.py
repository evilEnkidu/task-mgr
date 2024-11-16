# Generated by Django 5.1.2 on 2024-11-06 02:12

from django.db import migrations

def populate_statuses(apps, schema_editor):
    Status = apps.get_model('issues', 'Status')
    entries = {
        'to do': 'Work for this issue has not yet begun',
        'in progress': 'actively being worked on',
        'done': 'Issue completed'
        }
    for key, value in entries.items():
        status = Status(name=key, description=value)
        status.save()

class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_populate_priority'),
    ]

    operations = [
        migrations.RunPython(populate_statuses)
    ]
