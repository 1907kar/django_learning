from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookInstance, Author, Genre, Language
from django.views.generic import CreateView, DetailView, ListView
# for function based views
from django.contrib.auth.decorators import login_required
# for class based views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
    }
    return render(request, 'catalog/index.html', context=context)

# added mixin, so that only logged in user can create book  
class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    # for template its gonna look for model_form.html
    # Since success url is not provided, it gonna look for model_detail.html
    # So pls add that below by import DetailView

class BookDetail(DetailView):
    model = Book

@login_required
def restricted_view(request):
    return render(request, 'catalog/restricted_view.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    # THis login is not need to be added in urls.py as this is automatically added
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class UserCheckedOutBooks(LoginRequiredMixin, ListView):
    # Listing all the book instances BUT filter it based on currently logged in user
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 10

    # overriding default queryset to filter out the book instances based on currently logged in user
    def get_queryset(self):
        # for each session, request object is created with user, path... etc 
        return BookInstance.objects.filter(borrower=self.request.user).all()
    