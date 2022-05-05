from django.shortcuts import redirect, render
from django.views.generic import ListView
from ankiety.forms import Formularz0
from ankiety.forms import Formularz1
from ankiety.forms import Formularz2
from ankiety.forms import Formularz3
from ankiety.forms import Formularz4
from ankiety.forms import Formularz5
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
        form0 = Formularz0()
        form1 = Formularz1()
        form2 = Formularz2()
        form3 = Formularz3()
        form4 = Formularz4()
        form5 = Formularz5(initial={
            'wiek': 20
        })
    else:
        form0 = Formularz1(request.POST)
        form1 = Formularz1(request.POST)
        form2 = Formularz1(request.POST)
        form3 = Formularz1(request.POST)
        form4 = Formularz1(request.POST)
        form5 = Formularz1(request.POST)
        if form0.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            print('Hura!')

            # odp = Odpowiedz()
            # odp.wiek = form.cleaned_data['wiek']
            # odp.plec = form.cleaned_data['plec']
            # odp.wyksztalcenie = form.cleaned_data['wyksztalcenie']
            # odp.save()
            form0.save()
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()
            return redirect('dziekuje')

    return render(request, 'wypelnij.html', {
        'form0': form0,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5
    })


def wyniki(request):
    odpowiedzi = Odpowiedz.objects.all()

    return render(request, 'wyniki.html', {
        'odpowiedzi': odpowiedzi
    })


def dziekuje(request):
    return render(request, 'dziekuje.html')

