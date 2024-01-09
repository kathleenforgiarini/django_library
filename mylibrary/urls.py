from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path("book/<int:received_id>/", views.book_instance, name="book_instance"),
    path("authors/", views.authors, name="authors"),
]
