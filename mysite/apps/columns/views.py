from django.shortcuts import render, redirect
from columns.forms import ColumnForm
from columns.models import Column


def column_new(request):
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


def show(request):
    columns = Column.objects.all()
    return render(request, "show.html", {'columns': columns})  # надо чем-то заменить


def edit(request, id):
    column = Column.objects.get(id=id)
    return render(request, 'edit.html', {'column': column})


def update(request, id):
    column = Column.objects.get(id=id)
    form = ColumnForm(request.POST, instance=column)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'column': column})


def destroy(request, id):
    column = Column.objects.get(id=id)
    column.delete()
    return redirect("/")
