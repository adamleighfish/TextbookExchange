from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from rest_framework import routers

from home import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'listing', views.ListingViewSet)
router.register(r'exchange', views.ExchangeViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'school', views.SchoolViewSet)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.add_user, name='signup'),
    url(r'^school/$', views.StudentSchoolView.as_view(), name='school'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^about/', views.about, name='about'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^add_listing/', views.add_listing, name='add_listing'),
    url(r'^login/$', login, {'template_name': 'home/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^autocomplete/get_book/', views.AutoCompleteView.as_view(), name='get_book'),
    url(r'^api/', include(router.urls)),
    url(r'^listing_list/$', views.ListBooks.as_view(), name='booksearch'),
    url(r'^ajax/find_books/$', views.find_books, name='find_books'),
]
