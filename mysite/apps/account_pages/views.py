from django.shortcuts import render


def main(request):
    return render(request, 'account_pages/home.html')