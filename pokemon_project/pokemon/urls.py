from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main-page'),
    path('wiki', views.wiki_page, name='wiki-page')
    ]

