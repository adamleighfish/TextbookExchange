import json

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from home.forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Book, Student, Listing, Exchange, School
from .serializers import BookSerializer, StudentSerializer, ListingSerializer, ExchangeSerializer, \
    UserSerializer, SchoolSerializer


def home(request):
    session_language = 'en'
    request.session['lang'] = session_language

    return render(request, "home/home.html", {'session_language': session_language})


def about(request):
    session_language = 'en'
    request.session['lang'] = session_language

    return render(request, "about/about.html", {'session_language': session_language})


def dashboard(request):
    session_language = 'en'
    request.session['lang'] = session_language

    return render(request,'dashboard/dashboard.html', {'session_language': session_language})


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'register/register.html', {'user_form':user_form,
                                                      'registered': registered})


def user_login(request):
    session_language = 'en'
    request.session['lang'] = session_language

    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard/dashboard.html'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details")
    else:
    '''
    render(request, 'login/login.html', {'session_language': session_language})


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
        query = self.request.GET.get('q')
        if query:
            result = Listing.objects.filter(bid__title__iexact=query)
        return result
