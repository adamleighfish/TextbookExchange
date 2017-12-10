# TextbookExchange/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls', namespace="home")),
    url(r'^messages/', include('postman.urls', namespace="postman", app_name='postman'))

]
