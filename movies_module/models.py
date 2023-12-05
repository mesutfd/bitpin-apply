from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

from accounts_module.models import User

# Create your models here.
from django.urls import reverse


class MoviesCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    popularity = models.IntegerField(default=98, verbose_name='محبوبیت')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f'( {self.title} - %{self.popularity} )'

    def representor(self):
        return f'( {self.title} - %{self.popularity} )'


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


rating_choices = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


class Movies(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام فیلم')
    director = models.CharField(max_length=300, verbose_name="کارگردان")
    category = models.ManyToManyField(MoviesCategory, verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='بنر')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='خلاصه داستان')
    description = models.TextField(verbose_name='توضیحات', db_index=True)
    slug = models.SlugField(null=False, db_index=True, max_length=400, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} اثر ({self.director})"

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم ها'


class Rating(models.Model):
    score = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ],
    )
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")

    def __str__(self):
        return str(self.pk)

    def average_rating(self):
        avg_score = Rating.objects.filter(movie=self.movie).aggregate(Avg('score'))['score__avg']
        return avg_score if avg_score is not None else 0
