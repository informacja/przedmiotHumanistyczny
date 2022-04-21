from django.shortcuts import redirect, render

from ankiety.forms import Formularz
from ankiety.models import Odpowiedz


def home(request):
    return render(request, 'home.html', {
    })


def wypelnij(request):
    print('GET:', request.GET)
    print('POST:', request.POST)

    if request.method == 'GET':
        form = Formularz(initial={
            'wiek': 20
        })
    else:
        form = Formularz(request.POST)
        if form.is_valid():
            print('Hura!')

            # odp = Odpowiedz()
            # odp.wiek = form.cleaned_data['wiek']
            # odp.plec = form.cleaned_data['plec']
            # odp.wyksztalcenie = form.cleaned_data['wyksztalcenie']
            # odp.save()
            form.save()
            return redirect('dziekuje')

    return render(request, 'wypelnij.html', {
        'form': form
    })


def wyniki(request):
    odpowiedzi = Odpowiedz.objects.all()

    return render(request, 'wyniki.html', {
        'odpowiedzi': odpowiedzi
    })


def dziekuje(request):
    return render(request, 'dziekuje.html')
