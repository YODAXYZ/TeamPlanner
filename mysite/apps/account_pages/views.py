from django.http.response import Http404
from django.shortcuts import render
from boards.models import Board


def main(request):
    return render(request, 'account_pages/home.html')


def create_board(request):
    return render(request, "account_pages/create_board.html", {})


def board_list(request):
    return render(request, 'index.html')


def index(request):
    board_list = Board.objects.order_by('pub_date')
    return render(request, 'account_pages/board_list.html', {'board_list': board_list})


def detail(request, board_id):
    try:
        a = Board.objects.get(id=board_id)
    except:
        raise Http404("404 error !!!")

    return render(request, 'board/detail.html', {'board': a})
