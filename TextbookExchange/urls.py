# TextbookExchange/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls', namespace="home")),
    url(r'^register/', include('register.urls', namespace="register")),
    url(r'^login/', include('login.urls', namespace="login")),
    url(r'^dashboard/', include('dashboard.urls')),
]
