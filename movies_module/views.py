from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import ListView
from movies_module.models import Movies, Rating


class MoviesListView(ListView):
    pass
    template_name = 'movies_module/index.html'
    model = Movies
    context_object_name = 'movies'
    ordering = ['-id']
    paginate_by = 6


def rate_movie(request: HttpRequest):
    if request.user.is_authenticated:
        if request.method == 'POST':
            el_id = request.POST.get('el_id')
            print(el_id)
            val = request.POST.get('val')
            print(val)
            obj = Rating.objects.filter(movie_id=el_id).first()
            obj.score = val
            obj.user = request.user
            obj.save()
            return JsonResponse({
                'success': 'true',
                'score': val,

            }, safe=False)

    else:
        return redirect(reverse('login_page'))
