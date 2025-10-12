from django.urls import path
from .views import TravellingSalesmanView

urlpatterns = [
    path("travel/", TravellingSalesmanView.as_view(), name="tsp_result"),
]
