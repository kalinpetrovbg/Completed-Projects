from django.shortcuts import render, redirect

from second_todo.second.forms import CreatePlace
from second_todo.second.models import Place


def home_page(request):
    places = Place.objects.all()
    context = {
        'places': places,
    }
    return render(request, 'index.html', context)

def list_view(request):
    all_places = Place.objects.all()

    context = {
        'places': all_places,
    }
    return render(request, 'list.html', context)

def detail_view(request, pk):
    place = Place.objects.get(pk=pk)

    context = {
        'place': place,
    }
    return render(request, 'detail.html', context)

def add_place(request):
    add_form = CreatePlace(request.POST)
    context = {
        'form': add_form,
    }
    return render(request, 'add.html', context)

def create_from_form(request):
    name = request.POST['name']
    location = request.POST['location']
    distance_from_sofia = request.POST['distance']
    img = request.POST['img_url']

    place = Place(name=name, location=location, distance=distance_from_sofia, img_url=img)
    place.save()
    return redirect('/')

def remove_place(request):
    all_places = Place.objects.all()
    context = {
        'places': all_places,
    }
    return render(request, 'remove.html', context)

def delete_from_form(request):
    search = request.POST['name']
    found = Place.objects.filter(name=search).first()
    if found:
        found.delete()
    return redirect('/')