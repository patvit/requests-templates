from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv
import os

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице


    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        BUS_STATIONS = []
        for row in reader:
            BUS_STATIONS.append(row)

        paginator = Paginator(BUS_STATIONS, 10)
        page_number = int(request.GET.get("page", 2))
        page = paginator.get_page(page_number)

        context = {
            'page': page,
            'bus_stations': page,
        }

    return render(request, 'stations/index.html', context)

