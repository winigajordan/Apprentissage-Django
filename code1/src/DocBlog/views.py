from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def index (request):
    #return HttpResponse('<h1>bonjour index</h1>')
    date = datetime.today()
    return render(
        request,
        "DocBlog/index.html",
        context={
            "nom":"rema",
            "prenom": "jordan",
            "date": date
        })

def vue_de_test(request):
    return HttpResponse('<h1>bonjour</h1>')