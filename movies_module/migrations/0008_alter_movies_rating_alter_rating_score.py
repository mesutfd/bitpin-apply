# Generated by Django 4.1.2 on 2022-10-17 08:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_module', '0007_alter_movies_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_rating_score', to='movies_module.rating', verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
