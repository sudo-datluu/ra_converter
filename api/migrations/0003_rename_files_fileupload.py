# Generated by Django 5.0.3 on 2024-03-17 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_path_files_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='FileUpload',
        ),
    ]