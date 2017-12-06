from rest_framework import serializers
from .models import Book, Student, Listing, Exchange

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url','title', 'ISBN')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url','fname', 'lname', 'school', 'email')

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ('url', 'sid', 'bid', 'type', 'date', 'open')
        read_only_fields = ('sid','bid','date')

class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exchange
        fields = ('url','sid1','bid1','sid2','bid2','date')
        read_only_fields = ('url','sid1','bid1','sid2','bid2','date')
