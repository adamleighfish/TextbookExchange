import json
import operator
from functools import reduce


from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from home.forms import UserForm, SchoolForm
from home.models import Book, Student, Listing, Exchange, School
from home.serializers import BookSerializer, StudentSerializer, ListingSerializer, ExchangeSerializer, \
    UserSerializer, SchoolSerializer


def home(request):
    return render(request, 'home/home.html', {})


class SignUpView(CreateView):
    template_name = 'home/signup.html'
    form_class = UserForm
    success_url = '/school/'


class StudentSchoolView(FormView):
    template_name = 'home/school.html'
    form_class = SchoolForm
    success_url = '/dashboard/'

class AboutView(CreateView):
    template_name = 'home/about.html'


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


class DashboardView(CreateView):
    template_name = 'home/dashboard.html'


def about(request):
    return render(request, 'home/about.html', {})


def dashboard(request):
    listings = Listing.objects.all()
    return render(request, 'home/dashboard.html', {'listings': listings})


class AutoCompleteView(FormView):
    def get(self, request, *args, **kwargs):
        data = request.GET
        bookname = data.get("term")
        if bookname:
            books = Book.objects.filter(title__contains=bookname)
        else:
            books = Book.objects.all()

        results = []
        for book in books:
            book_json = {'id': book.id, 'label': book.title, 'value': book.title}
            results.append(book_json)
            data = json.dumps(results)
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class StudentViewSet(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ListingViewSet(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated,)
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ExchangeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ListBooks(ListView):
    paginate_by = 10
    template_name = 'home/listing_list.html'
    context_object_name = 'result'

    def get_queryset(self):
        result = Listing.objects.all()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(reduce(operator.and_, (Q(bid__title__icontains=q) for q in query_list)))

        return result

