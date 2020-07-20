from django.http.response import Http404
from django.shortcuts import render, redirect
from boards.models import Board
from columns.models import Column
from tasks.models import Task
from .forms import BoardForm
from django.utils import timezone


def detail(request, board_id):
    if request.user.is_authenticated:
        a = Board.objects.get(id=board_id)
        if a in request.user.board.all():
            columns_list = Column.objects.filter(board=board_id)
            # task_list = list()
            # for column in columns_list:
            #     task_list.append(Task.objects.filter(column=column))
            task_list = Task.objects.all()

            return render(request, 'boards/detail.html', {'board': a, 'columns_list': columns_list, 'task_list': task_list})
        else:
            return render(request, "account_pages/warning.html")
    else:
        return redirect("/login")


def create_board(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BoardForm(request.POST)
            if form.is_valid():
                board = form.save(commit=False)
                board.pub_date = timezone.now()
                board.user = request.user
                board.save()
                request.user.board.add(board)
            return redirect("/")
        else:
            form = BoardForm()
        return render(request, "boards/create_board.html", {"form": form})
    else:
        return redirect("/login")
