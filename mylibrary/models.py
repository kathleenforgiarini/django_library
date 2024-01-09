from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Reserved = "r"
    Booked = "b"
    Available = "a"
    status_choices = [
        (Reserved, "Reserved"),
        (Booked, "Booked"),
        (Available, "Available"),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default=Available)
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.book.title
