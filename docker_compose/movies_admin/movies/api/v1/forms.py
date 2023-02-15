from django.forms import ModelForm
from movies.models import FilmWork


class ArticleForm(ModelForm):
    class Meta:
        model = FilmWork
        fields = ['pub_date', 'headline', 'content', 'reporter']