from django.urls import path
from .views import ListingsViews, ListingView, SearchView
urlpatterns = [
    path("", ListingsViews.as_view(), name="listings"),
    path('search/', SearchView.as_view(), name='search'),
    path('<slug>', ListingView.as_view(), name='listing')
]
