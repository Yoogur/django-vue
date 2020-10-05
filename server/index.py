from django.shortcuts import render


def IndexPrint(request):
    return render(request, "app/templates/mypage.html")