from django.shortcuts import render, redirect
from tasks.forms import CommentForm, TaskForm
from tasks.models import Comment, Task
from django.utils import timezone


def index(request):
    pass
    # room_list = Room.objects.order_by('pub_date')[:5]
    # return render(request, 'room/list.html', {'room_list': room_list})


def create_task(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.pub_date = timezone.now()
                task.user = request.user
                # task.lead_time = timezone.now()
                task.save()
                # task_instance = Task.objects.create(author=request.user, title=form.data['title'], column=form.data['column'], pub_date=form.data['pub_date'])
                # request.user.tasks.add(task)  # хз, как добавить в бд
                # Task.objects.create(task)
            return redirect("/")
        else:
            form = TaskForm()
            return render(request, "tasks/create_task.html", {'form': form})
    else:
        return redirect("/login")


def edit_comment(request, id):
    comment = Comment.objects.get(id=id)
    return render(request, 'edit.html', {'comment': comment})


def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'comment': comment})


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect("/show_comment")
