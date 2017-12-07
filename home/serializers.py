from django.contrib.auth.models import User
from rest_framework import serializers

from home.models import Book, Student, Listing, Exchange, School


class BookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="home:book-detail")

    class Meta:

        model = Book
        fields = ('url', 'title', 'ISBN')


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="home:school-detail")

    class Meta:

        model = School
        lookup_field = 'school'
        fields = ('url', 'school', 'state', 'city')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="home:user-detail")

    class Meta:

        model = User
        lookup_field = 'username'
        fields = ('url', 'username')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="home:student-detail")
    user = UserSerializer()
    school = SchoolSerializer()

    class Meta:

        model = Student
        fields = ('url', 'user', 'school')


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="home:listing-detail")
    sid = StudentSerializer()
    bid = BookSerializer()

    class Meta:

        model = Listing
        fields = ('url', 'sid', 'bid', 'type', 'date', 'open')
        read_only_fields = ('sid', 'bid', 'date')


class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="home:exchange-detail")
    bid1 = BookSerializer()
    bid2 = BookSerializer()
    sid1 = StudentSerializer()
    sid2 = StudentSerializer()

    class Meta:

        model = Exchange
        fields = ('url', 'sid1', 'bid1', 'sid2', 'bid2', 'date')
        read_only_fields = ('url', 'sid1', 'bid1', 'sid2', 'bid2', 'date')
