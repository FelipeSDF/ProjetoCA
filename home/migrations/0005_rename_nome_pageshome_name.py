# Generated by Django 5.1.1 on 2024-09-24 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_pageshome_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageshome',
            old_name='nome',
            new_name='name',
        ),
    ]
