from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_phrase/', views.add_phrase, name='Flashcards-add_phrase'),
    path('about/', views.about, name='Flashcards-about'),
    path('phrases/', views.phrases, name='Flashcards-phrases'),
    path('words/', views.words, name='Flashcards-words'),
    path('free/', views.free, name='Flashcards-free'),
    path('glossary/', views.glossary, name='Flashcards-glossary'),
    path('add_words/', views.add_word, name='Flashcards-add_word')
]
