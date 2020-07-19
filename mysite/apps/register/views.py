from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                                )
            login(request, user)
            return redirect("/")
=======
            form.save()

        return redirect("/")
>>>>>>> origin
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})

