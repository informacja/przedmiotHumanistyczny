from django.shortcuts import redirect, render
from django.views.generic import ListView
from ankiety.forms import Formularz
from ankiety.models import Odpowiedz
from django.core.paginator import Paginator

class OdpowiedzListView(ListView):
    paginate_by = 2
    model = Odpowiedz

def listing(request):
    contact_list = Odpowiedz.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'template.html', {'page_obj': page_obj})

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

