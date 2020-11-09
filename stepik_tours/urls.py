from django.urls import path
from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('', MainView),
    path('departure/<str:departure>', DepartureView),
    path('tour/<int:id>', TourView),
]
