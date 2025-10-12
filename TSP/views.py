from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from TSP.utils import TravellingSalesmanSolver

class TravellingSalesmanView(View):
    def get(self, request):
        solver = TravellingSalesmanSolver()
        result = solver.find_shortest_route()
        return JsonResponse(result)