# Generated by Django 4.1.2 on 2022-10-17 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_module', '0009_alter_rating_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='movies_module.movies'),
            preserve_default=False,
        ),
    ]
