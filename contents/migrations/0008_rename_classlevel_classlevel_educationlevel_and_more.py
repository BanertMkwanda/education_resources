# Generated by Django 5.1.4 on 2025-01-06 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_rename_class_grade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classlevel',
            old_name='classlevel',
            new_name='educationlevel',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='document',
            new_name='resourcetype',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='educationalevel',
            new_name='classlevel',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject',
            new_name='grade',
        ),
        migrations.RemoveField(
            model_name='resourcetype',
            name='resourcetype',
        ),
        migrations.AddField(
            model_name='resourcetype',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contents.subject'),
            preserve_default=False,
        ),
    ]
