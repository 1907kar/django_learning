from django.db import models
from django.urls import reverse
# for accessing users
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

     
class Book(models.Model):
    title = models.CharField(max_length=200)
    # This is written in foreign key, as one author has more than one book written and can be linked
    # on_delete is SET_NULL, what this means is, if we delete the author, it sets null to all the linked one
    # SET_NULL helps to store null value to the books incase no author is provided
    # CASCADE helps to remove associated model books as well
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=600)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    # connecting Genre i.e this is not like (foreign key) linking it is mapping more than one option from the db
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pk}: {self.title}"
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"pk": self.pk})

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)

    # This is for sorting of the models
    class Meta:
        ordering = ['last_name', 'first_name']    

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
    # This is for getting url to check on author details
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    
# Below is book instance, which helps to track the book borrow process
import uuid

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # connecting to Book
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    # configuring book instance to an user
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', "Maintenance"),
        ('o', "onloan"),
        ('a', "availale"),
        ('r', "reserved"),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')

    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        # Here title is fetched from book model class as it is refered as foreign key
        return f"{self.id=} ({self.book.title=})"
