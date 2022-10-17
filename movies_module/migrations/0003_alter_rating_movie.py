# Generated by Django 4.1.2 on 2022-10-17 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_module', '0002_remove_movies_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='movie_rating_score', to='movies_module.movies', verbose_name='فیلم'),
        ),
    ]
