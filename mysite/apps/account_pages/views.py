from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from boards.models import Board
from columns.models import Column
from .forms import BoardForm
from django.utils import timezone


def main(request):
    board_list = Board.objects.order_by('pub_date')
    column_list = Column.objects.all()
    return render(request, 'account_pages/home.html', {'board_list': board_list, 'column_list': column_list})


def create_board(request):
    if request.user.is_authenticated:
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.pub_date = timezone.now()
            board.user = request.user
            board.save()
        return HttpResponseRedirect("/")
    #     return render(request, "account_pages/create_board.html", {"form": form})
    else:
        return redirect("/login")


# def board_list(request):
#     return render(request, 'index.html')


# def index(request):
#     board_list = Board.objects.order_by('pub_date')
#     return render(request, 'account_pages/board_list.html', {'board_list': board_list})


def detail(request, board_id):
    try:
        a = Board.objects.get(id=board_id)
    except:
        raise Http404("404 error !!!")

    return render(request, 'board/detail.html', {'board': a})
