from django.shortcuts import HttpResponse, redirect, render # agrega redirección a la declaración de importación
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
    if request.method == "GET":
        random_word = "GENERADOR DE PALABRAS"
        request.session['counter']=0
    if request.method == "POST":
        random_word = get_random_string(length=14)
        request.session['counter']=request.session['counter'] + 1
    context = {
        "palabra_random": random_word,
    }
    return render(request,'index.html',context)


def redirige(request):
    return redirect("/random_word")


def reset(request):
    random_word = "GENERADOR DE PALABRAS"
    request.session['counter']=0
    return redirect("/random_word")

