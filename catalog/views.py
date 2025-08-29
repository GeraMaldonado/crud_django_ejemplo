#from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import Movie, Genre

class MovieList(generic.ListView):
    model = Movie
    paginate_by = 20
    template_name = "catalog/movie_list.html"

    def get_queryset(self):
        qs = Movie.objects.prefetch_related("genres").order_by("-vote_average")
        q = self.request.GET.get("q")
        gid = self.request.GET.get("genre")
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(original_title__icontains=q) |
                Q(imdb_id__icontains=q)
            )
        if gid:
            qs = qs.filter(genres__id=gid)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["genres"] = Genre.objects.order_by("name")
        ctx["q"] = self.request.GET.get("q", "")
        ctx["genre_selected"] = self.request.GET.get("genre", "")
        return ctx

class MovieDetail(generic.DetailView):
    model = Movie
    template_name = "catalog/movie_detail.html"

