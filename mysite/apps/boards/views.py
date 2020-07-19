from django.http.response import Http404
from django.shortcuts import render
from boards.models import Board


def detail(request, board_id):
    try:
        a = Board.objects.get(id=board_id)
    except:
        raise Http404("404 error !!!")
    if request.user.is_authenticated:
        return render(request, 'boards/detail.html', {'board': a})
    else:
        return render(request, 'account_pages/home.html')
