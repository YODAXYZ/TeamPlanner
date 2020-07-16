from django.shortcuts import render, redirect
from tasks.forms import CommentForm
from tasks.models import Comment


def index(request):
    pass
    # room_list = Room.objects.order_by('pub_date')[:5]
    # return render(request, 'room/list.html', {'room_list': room_list})


def create_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_comment')
            except:
                pass
    else:
        form = CommentForm()
    return render(request, 'index.html', {'form': form})


# def show(request):
#     employees = Comment.objects.all()
#     return render(request, "show.html", {'comments': comments})


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
