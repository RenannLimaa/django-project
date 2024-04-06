# Generated by Django 5.0.2 on 2024-04-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_alter_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='task',
            name='task_id',
            field=models.BigAutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]