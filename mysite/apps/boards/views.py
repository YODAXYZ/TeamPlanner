from django.http.response import Http404
from django.shortcuts import render
from boards.models import Board

def board_list(request):
    return render(request, 'index.html')


def index(request):
    board_list = Board.objects.order_by('pub_date')[:5]
    return render(request, 'boards/board_list.html', {'board_list': board_list})


def detail(request, board_id):
    pass
    try:
        a = Board.objects.get(id=board_id)
    except:
        raise Http404("404 error !!!")

    return render(request, 'board/detail.html', {'board': a})
