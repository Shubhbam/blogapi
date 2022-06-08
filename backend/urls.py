import imp
from django.urls import URLPattern, path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('articles',ArticleList.as_view()),
    path('articles/<slug:slug>',ArticleDetails.as_view())
]