from django.http.response import Http404
from django.shortcuts import render, redirect
from boards.models import Board
from columns.models import Column
from account_pages.forms import BoardForm
from django.utils import timezone


def detail(request, board_id):
    try:
        a = Board.objects.get(id=board_id)
        columns_list = Column.objects.filter(board=board_id)
        if request.user.is_authenticated:
            return render(request, 'boards/detail.html', {'board': a, 'columns_list': columns_list})
        else:
            return render(request, 'account_pages/home.html')
    except:
        raise Http404("404 error !!!")


def create_board(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BoardForm(request.POST)
            if form.is_valid():
                board = form.save(commit=False)
                board.pub_date = timezone.now()
                board.user = request.user
                board.save()
            return redirect("/")
        else:
            form = BoardForm()
        return render(request, "boards/create_board.html", {"form": form})
    else:
        return redirect("/login")



