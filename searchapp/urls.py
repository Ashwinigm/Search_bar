from django.urls import path

from .views import HomePageView, SearchResultsView, CreateRoomsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('', CreateRoomsView.as_view(), name='create_room')
]