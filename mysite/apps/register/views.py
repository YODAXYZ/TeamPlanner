from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            form.save()

            return redirect("/")  # Что тут нужно выкидывать?
        else:
            form = RegisterForm()

        return render(response, "register/register.html", {"form": form})
=======
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                                )
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})

>>>>>>> e5d237648e7b4d7b2431fd6790e535620ccb090f
