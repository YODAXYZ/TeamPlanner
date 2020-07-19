from django.http.response import Http404
from django.shortcuts import render, redirect
from boards.models import Board
from account_pages.forms import BoardForm
from django.utils import timezone


def detail(request, board_id):
    try:
        a = Board.objects.get(id=board_id)
    except:
        raise Http404("404 error !!!")

    return render(request, 'boards/detail.html', {'board': a})


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



