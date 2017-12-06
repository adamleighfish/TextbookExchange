import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Book, Student, Listing, Exchange
from .serializers import BookSerializer, StudentSerializer, ListingSerializer, ExchangeSerializer


# Create your views here.
def home(request):
    session_language = 'en'
    request.session['lang'] = session_language

    return render(request, "home/home.html", {'session_language': session_language})


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
            book_json = {}
            book_json['id'] = book.id
            book_json['label'] = book.title
            book_json['value'] = book.title
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