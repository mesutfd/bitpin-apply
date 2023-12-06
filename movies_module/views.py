from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from movies_module.models import Movies, Rating


class MoviesListView(ListView):
    pass
    template_name = 'movies_module/index.html'
    model = Movies
    context_object_name = 'movies'
    ordering = ['-id']
    paginate_by = 1

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     movies = Movies.objects.all()
    #     rates = Rating.objects.all()
    #     movie_rates = {}
    #     for rate in rates:
    #         for movie in movies:
    #             if movie.id == rate.movie_id:
    #                 movie_rates[str(movie.id)] = rate
    #     context['all_ratings'] = movie_rates
    #
    #     return context


class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movies_module/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_movie = self.object

        current_rate = Rating.objects.filter(movie_id=current_movie.id).first().score

        context['current_rate'] = current_rate

        return context


def rate_movie(request: HttpRequest):
    if request.user.is_authenticated:
        if request.method == 'POST':
            el_id = request.POST.get('el_id')
            print(el_id)
            val = request.POST.get('val')
            print(val)
            new_rate, is_created_now = Rating.objects.get_or_create(movie_id=el_id, user_id=request.user.id)
            if is_created_now:
                new_rate.score = val
                new_rate.save()

            else:
                obj = Rating.objects.filter(movie_id=el_id, user_id=request.user.id).first()
                new_rate.score = val
                new_rate.user = request.user
                new_rate.save()

            return JsonResponse({
                'success': 'true',
                'score': val,

            }, safe=False)

    else:
        return redirect(reverse('login_page'))
