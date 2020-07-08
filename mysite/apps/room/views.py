from django.shortcuts import render
from .models import Room
from django.http import HttpResponseRedirect, Http404


def index(request):
    room_list = Room.objects.order_by('pub_date')[:5]
    return render(request, 'room/list.html', {'room_list': room_list})


def detail(request, room_id):
    try:
        a = Room.objects.get(id=room_id)
    except:
        raise Http404("404 error !!!")

    return render(request, 'room/detail.html', {'room': a})
