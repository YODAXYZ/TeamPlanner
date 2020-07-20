from django.shortcuts import render, redirect
from .forms import ColumnForm
from .models import Column
from boards.models import Board
# from columns.forms import TaskForm
from tasks.models import Task


def create_column(request, board_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            board = Board.objects.get(id=board_id)
            form = ColumnForm(request.POST)
            if form.is_valid():
                column = form.save(commit=False)
                column.board = board
                column.save()
                board.column.add(column)
                # return redirect("/")
                # return render(request, "/boards/detail.html", {"board_id" : board_id})
                return redirect('/boards/{}'.format(board_id))
        else:
            form = ColumnForm()
        return render(request, "columns/create_column.html", {"form": form})
    else:
        return redirect("/login")


def detail(request, column_id, board_id):
    if request.user.is_authenticated:
        a = Column.objects.get(id=column_id)
        board = Board.objects.get(id=board_id)
        if a in board.column.all():
            task_list = Task.objects.filter(column=column_id)
            return render(request, 'columns/detail.html', {'column': a, 'task_list': task_list})
        else:
            return render(request, "account_pages/warning.html")
    else:
        return redirect("/login")


def edit_column(request, id):
    column = Column.objects.get(id=id)
    return render(request, 'edit.html', {'column': column})


def update_column(request, id):
    column = Column.objects.get(id=id)
    form = ColumnForm(request.POST, instance=column)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'column': column})


def delete_column(request, id):
    column = Column.objects.get(id=id)
    column.delete()
    return redirect("/")


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')  # не уверен, что тут вставлять
            except:
                pass
    else:
        form = TaskForm()
    return render(request, 'index.html', {'form': form})


# def show_task(request):
#     tasks = Task.objects.all()
#     return render(request, "show.html", {'tasks': tasks})


def edit_task(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'edit.html', {'task': task})


def update_task(request, id):
    task = Task.objects.get(id=id)
    form = ColumnForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'task': task})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/")

