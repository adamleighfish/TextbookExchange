from django.conf.urls import url, include
from home import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'listing', views.ListingViewSet)
router.register(r'exchange', views.ExchangeViewSet)

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^autocomplete/get_book/', views.AutoCompleteView.as_view(), name = 'get_book'),
    url(r'^api/', include(router.urls)),
    url(r'^search_results', views.ListBooks.as_view(), name = 'booksearch')
]
