from django.shortcuts import render, redirect
from columns.forms import ColumnForm
from columns.models import Column
from columns.forms import TaskForm
from tasks.models import Task


def create_column(request):
    if request.method == "POST":
        form = ColumnForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')  # не уверен, что тут вставлять
            except:
                pass
    else:
        form = ColumnForm()
    return render(request, 'index.html', {'form': form})


# def show_column(request):
#     columns = Column.objects.all()
#     return render(request, "show.html", {'columns': columns})  # надо чем-то заменить


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

