# Generated by Django 4.1.2 on 2022-10-17 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_module', '0005_remove_rating_movie_movies_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_rating_score', to='movies_module.rating', verbose_name='امتیاز'),
        ),
    ]
