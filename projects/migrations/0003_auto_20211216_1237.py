# Generated by Django 3.2.9 on 2021-12-16 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211216_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='variableextraction',
            name='project',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='variable_extractions', to='projects.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variableextraction',
            name='variable_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variable_extractions', to='projects.variableset'),
        ),
        migrations.AlterField(
            model_name='variableset',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variable_sets', to='projects.project'),
        ),
    ]
