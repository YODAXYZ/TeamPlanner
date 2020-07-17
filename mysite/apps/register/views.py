from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
<<<<<<< HEAD

        return redirect("/")
=======
            return redirect("/")  # Что тут нужно выкидывать?
>>>>>>> 3c4707e3318c3ac16d73f54741bb2ea3f10215d4
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
