from django import forms
from .models import Movie, Genre

class DateInput(forms.DateInput):
    input_type = "date"

class MovieForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.order_by("name"),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Géneros",
    )

    class Meta:
        model = Movie
        fields = [
            "tmbd_id", "imdb_id", "title", "original_title", "overview",
            "release_date", "runtime", "budget", "revenue",
            "popularity", "vote_average", "vote_count",
            "homepage", "poster_path", "genres",
        ]
        widgets = {
            "release_date": DateInput(),
        }

