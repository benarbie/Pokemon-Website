from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main-page'),
    path('wiki/<int:entry>', views.wiki_page_entry, name='wiki-pag-entry'),
    path('wiki/<str:name>', views.wiki_page_name, name='wiki-page-name')
    ]

