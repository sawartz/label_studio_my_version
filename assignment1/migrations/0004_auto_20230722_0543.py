# Generated by Django 3.2.19 on 2023-07-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0003_alter_assignment_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='assignment',
            name='assigned_user_email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assigned_user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='project_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='project_id',
            field=models.IntegerField(null=True),
        ),
    ]
