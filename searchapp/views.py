from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Rooms


class HomePageView(TemplateView):
    template_name = 'home.html'

# class SearchResultsView(ListView):
#     model = Rooms
#     template_name = 'search_results.html'
#     queryset = Rooms.objects.filter(room_name__icontains='Two')
#
#     def get_queryset(self):  # new
#         return Rooms.objects.filter(name__icontains='Two')

# class SearchResultsView(ListView):
#     model = Rooms
#     template_name = 'search_results.html'
#
#     def get_queryset(self): # new
#         return Rooms.objects.filter(
#             Q(room_name__icontains='Two') | Q(genre__icontains='Rock')
#         )

class SearchResultsView(ListView):
    model = Rooms
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Rooms.objects.filter(
            Q(room_name__icontains=query) | Q(genre__icontains=query)
        )
        return object_list