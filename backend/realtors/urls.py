from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLResolver
from .views import RealtorListView, RealtorView, TopSellerView
urlpatterns = [
    path('', RealtorListView.as_view(), name='realtor-list'),
    path('topseller/', TopSellerView.as_view(), name='top-seller'),
    path('<int:pk>', RealtorView.as_view(), name='realtor')

]
