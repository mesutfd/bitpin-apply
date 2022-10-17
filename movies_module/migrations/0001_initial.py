# Generated by Django 4.1.2 on 2022-10-17 05:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='نام فیلم')),
                ('director', models.CharField(max_length=300, verbose_name='کارگردان')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='بنر')),
                ('rating', models.IntegerField(verbose_name='امتیاز')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='خلاصه داستان')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات')),
                ('slug', models.SlugField(max_length=400, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'فیلم',
                'verbose_name_plural': 'فیلم ها',
            },
        ),
        migrations.CreateModel(
            name='MoviesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_rating_score', to='movies_module.movies', verbose_name='فیلم')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='category',
            field=models.ManyToManyField(related_name='product_categories', to='movies_module.moviescategory', verbose_name='دسته بندی ها'),
        ),
    ]
