from django import forms
from django.core.exceptions import ValidationError

# from django.db.models import Model
from ankiety.models import Odpowiedz
from django.forms import models

class Formularz0(models.ModelForm):  # Przykładowy formularz

    name = forms.CharField()
    wiek = forms.IntegerField(min_value=18)
    Jakie_jest_twoje_zaufanie_do_szczepien = forms.ChoiceField(choices=[
        (1,"lubię"),
        (2,"Nie ufam"),
    ], widget=forms.RadioSelect)

    COLORS = (
        ('R', 'Red'),
        ('B', 'Yellow'),
        ('G', 'White'),
    )
    color = forms.MultipleChoiceField(choices=COLORS)

    class Meta:
        model = Odpowiedz
        fields = '__all__'

    def clean_wiek(self):
        wiek = self.cleaned_data.get('wiek', 0)
        if wiek % 2:
            raise ValidationError('Wiek musi być parzysty')
        return wiek

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color:
            raise forms.ValidationError("...")

        if len(color) > 2:
            raise forms.ValidationError("...")

        color = ''.join(color)
        return color

class Formularz1(models.ModelForm):

    Jak_oceniasz_swój_stosunek_do_szczepień_innych_niż_na_Covid = forms.MultipleChoiceField(choices=[
        ('1', 'zdecydowanie negatywny'),
        ('2', 'raczej negatywny'),
        ('3', 'neutralny'),
        ('4', 'raczej pozytywny'),
         ('5', 'zdecydowanie pozytywny'),
    ])
    #
    # Czy_byłaś/eś_szczepiona/y_zgodnie_z_kalendarzem_szczepień? = forms.ChoiceField(choices=[
    #     (1, 'tak'),
    #     (2, 'Nie'),
    #     (3, 'Nie pamiętam'),
    # ])
    #
    # Przeciw_jakim_chorobom_obowiązkowym_byłeś_szczepiona/y? = forms.MultipleChoiceField(choices=[
    #     (1, 'Wirusowe zapalenie wątroby typu B (WZW B)'),
    #     (2, 'Błonica'),
    #     (3, 'Gruźlica');
    #     (4, 'Tężec'),
    #     (5, 'Krztusiec (koklusz)'),
    #     (6, 'Polio (IPV)'),
    #     (7, 'Pałeczka hemofilna typu B (Hib)'),
    #     (8, 'Pneumokoki (PCV)'),
    #     (9, 'Odra'),
    #     (10, 'Świnka'),
    #     (11, 'Różyczka'),
    #     (12, 'Inne (podaj jakie) (pole do wpisywania)'),
    #     (13, 'Nie mam możliwości sprawdzenia'),
    # ])
    #
    # Czy_kiedykolwiek_przyjmowałaś/eś_szczepienia_nieobowiązkowe,_ale_zalecane? = forms.ChoiceField(choices=[
    #     (1, 'tak'),
    #     (2, 'Nie'),
    #     (3, 'Nie pamiętam'),
    # ])

    # Przeciw_jakim_chorobom_nieobowiązkowym_a_zalecanym_byłeś_szczepiona/y? = forms.MultipleChoiceField(choices=[
    #     (1, 'Rotawirusy'),
    #     (2, 'Grypa'),
    #     (3, 'Meningokoki'),
    #     (4, 'Ospa wietrzna'),
    #     (5, 'Wirusowe zapalenie wątroby typu A (WZW A)'),
    #     (6, 'Odkleszczowe zapalenie mózgu'),
    #     (7, 'Inne z wyjątkiem Covid  (podaj jakie) (pole do wpisania)'),
    #     (8, 'Nie mam możliwości sprawdzenia'),
    # ])

    # Czy_rekomendujesz_szczepienie_innym?  = forms.ChoiceField(choices=[
    #     (1, 'tak'),
    #     (2, 'Nie'),
    #     (3, 'Nie wiem'),
    # ])

    # Czy_w_przeszłości_doświadczyłaś/łeś_skutków_niepożądanych_przyjęcia_szczepionki? = forms.ChoiceField(choices=[
    #     (1, 'tak'),
    #     (2, 'Nie'),
    #     (3, 'Nie pamiętam'),
    # ])

    # Jeśli_tak,_to_jakich? = forms.MultipleChoiceField(choices=[
    #     (1, 'Gorączka'),
    #     (2, 'Zmęczenie, złe samopoczucie'),
    #     (3, 'Ból głowy'),
    #     (4, 'Ból mięśni'),
    #     (5, 'Ból stawów'),
    #     (6, 'Dreszcze'),
    #     (7, 'Dolegliwości ze strony układu pokarmowego (biegunka, mdłości, ból brzucha)'),
    #     (8, 'Ból w miejscu wstrzyknięcia/opuchlizna/zaczerwienienie w miejscu wstrzyknięcia'),
    #     (9, 'Nadmierne pocenie się'),
    #     (10, 'Swędzenie skóry lub wysypka'),
    #     (11, 'Powiększone węzły chłonne'),
    #     (12, 'Uczucie omdlenia lub oszołomienia'),
    #     (13, 'Trudności z oddychaniem'),
    #     (14, 'Świszczący oddech'),
    #     (15, 'Opuchlizna twarzy i gardła'),
    #     (16, 'Przyspieszenie akcji serca'),
    #     (17, 'Inne, jakie? (pole do wpisania)'),
    # ])

    # Czy_doświadczone_skutki_uboczne_zmieniły_twój_stosunek_do_szczepień? = forms.ChoiceField(choices=[
    #     (1, 'tak'),
    #     (2, 'Nie'),
    #     (3, 'Nie wiem'),
    # ])

    # Czy_rekomendujesz_szczepienie_innym_mimo_doświadczonych_skutków_ubocznych? = forms.ChoiceField(choices=[
    #     (1, 'tak'),
    #     (2, 'Nie'),
    #     (3, 'Nie wiem'),
    # ])

    # Szczepenia dzieci

    # Czy_posiadasz_dzieci? = forms.ChoiceField(choices=[
    #     (1, 'tak'),
    #     (2, 'Nie'),
    # ])

    # W_jakim_wieku_jest_Twoje_dziecko_(jeśli_posiadasz_więcej_niż_jedno,_zaznacz_wiek_najstarszego)? = forms.ChoiceField(choices=[
    #     (1, '0-3'),
    #     (2, '4-9'),
    #     (2, '10-14'),
    #     (2, '15-19'),
    # ])

    # Czy_szczepiłaś/łeś_lub_zamierzasz_zaszczepić_je_zgodnie_z_kalendarzem_szczepień_wszystkimi_obowiązkowymi_szczepionkami? = forms.ChoiceField(choices=[
    #     (1, 'Tak'),
    #     (2, 'Nie'),
    #     (3, 'Nie wiem'),
    # ])

    # Przec_wjakim_chorobom_z_szczepień_obowiązkowych_szczepiłaś/łeś_swoje_dzieci? = forms.MultipleChoiceField(choices=[
    #     (1, 'Wirusowe zapalenie wątroby typu B (WZW B)'),
    #     (2, 'Błonica'),
    #     (3, 'Gruźlica');
    #     (4, 'Tężec'),
    #     (5, 'Krztusiec (koklusz)'),
    #     (6, 'Polio (IPV)'),
    #     (7, 'Pałeczka hemofilna typu B (Hib)'),
    #     (8, 'Pneumokoki (PCV)'),
    #     (9, 'Odra'),
    #     (10, 'Świnka'),
    #     (11, 'Różyczka'),
    #     (12, 'Inne (podaj jakie) (pole do wpisywania)'),
    #     (13, 'Nie mam możliwości sprawdzenia'),
    # ])

    # Czy_szczepiłaś/eś/_lub_zamierzasz_zaszczepić_je_zalecanymi_szczepionkami_nieobowiązkowymi? = forms.ChoiceField(choices=[
    #     (1, 'Tak, szczepiłam/em'),
    #     (2, 'Nie, ale mam zamiar'),
    #     (3, 'Nie i nie mam zamiaru'),
    #     (4, 'Nie wiem'),
    # ])

    # Przeciw_jakim_chorobom_zalecanym_szczepiłaś/łeś_lub_chcesz_zaszczepić_swoje_dziecko?  = forms.MultipleChoiceField(choices=[
    #     (1, 'Rotawirusy'),
    #     (2, 'Grypa'),
    #     (3, 'Meningokoki'),
    #     (4, 'Ospa wietrzna'),
    #     (5, 'Wirusowe zapalenie wątroby typu A (WZW A)'),
    #     (6, 'Odkleszczowe zapalenie mózgu'),
    #     (7, 'Inne z wyjątkiem Covid  (podaj jakie) (pole do wpisania)'),
    #     (8, 'Nie mam możliwości sprawdzenia'),
    # ])

    class Meta:
        model = Odpowiedz
        fields = '__all__'

    def clean_wiek(self):
        wiek = self.cleaned_data.get('wiek', 0)
        if wiek % 2:
            raise ValidationError('Wiek musi być parzysty')
        return wiek

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color:
            raise forms.ValidationError("...")

        if len(color) > 2:
            raise forms.ValidationError("...")

        color = ''.join(color)
        return color

class Formularz2(models.ModelForm):

    class Meta:
        model = Odpowiedz
        fields = '__all__'


class Formularz3(models.ModelForm):
    class Meta:
        model = Odpowiedz
        fields = '__all__'


class Formularz4(models.ModelForm):
    class Meta:
        model = Odpowiedz
        fields = '__all__'


class Formularz5(models.ModelForm):
    class Meta:
        model = Odpowiedz
        fields = '__all__'




    #Dopisane/nie sprawdzone - po kolei jak w arkuszach


    #Szczepienie przeciw COVID-19

    #Jaki_jest_twój_stosunek_do_szczepienia_na_Covid? = forms.MultipleChoiceField(choices=[
    #     ('1', 'zdecydowanie negatywny'),
    #     ('2', 'raczej negatywny'),
    #     ('3', 'neutralny'),
    #     ('4', 'raczej pozytywny'),
    #      ('5', 'zdecydowanie pozytywny'),
    # ])

    #Czy_jesteś_zaszczepiona/y_przeciw_COVID-19? = forms.ChoiceField(choices=[
    #     (1, 'Tak, szczepiłam/em'),
    #     (2, 'Nie, ale mam zamiar'),
    #     (3, 'Nie i nie mam zamiaru'),
    #     (4, 'Nie wiem'),
    # ])
    
    #Jeśli_tak,_iloma_dawkami? = forms.ChoiceField(choices=[
    #     (1, '1'),
    #     (2, '2'),
    #     (3, '3'),
    # ])

    #Jeśli_tak,_jakimi_szczepionkami?
    # 1 dawka  = forms.ChoiceField(choices=[
    #     (1, 'Comirnaty (Pfizer-biontech)'),
    #     (2, 'COVID-19 Vaccine Moderna (Moderna)'),
    #     (3, 'Vaxzevria (astrazeneca)'),
    #     (2, 'COVID-19 Vaccine Janssen (Janssen Pharmaceutical Companies of Johnson & Johnson)'),
    #     (3, 'Inna'),
    # ])
    # 2 dawka  = forms.ChoiceField(choices=[
    #     (1, 'Comirnaty (Pfizer-biontech)'),
    #     (2, 'COVID-19 Vaccine Moderna (Moderna)'),
    #     (3, 'Vaxzevria (astrazeneca)'),
    #     (2, 'COVID-19 Vaccine Janssen (Janssen Pharmaceutical Companies of Johnson & Johnson)'),
    #     (3, 'Inna'),
    # ])
    # 3 dawka  = forms.ChoiceField(choices=[
    #     (1, 'Comirnaty (Pfizer-biontech)'),
    #     (2, 'COVID-19 Vaccine Moderna (Moderna)'),
    #     (3, 'Vaxzevria (astrazeneca)'),
    #     (2, 'COVID-19 Vaccine Janssen (Janssen Pharmaceutical Companies of Johnson & Johnson)'),
    #     (3, 'Inna'),
    # ])

    #Z_jakich_powodów_podjęłaś/eś_decyzję_o_szczepieniu? = forms.MultipleChoiceField(choices=[
    #     (1, 'Uchronienie się przed zachorowaniem'),
    #     (2, 'Uchronienie się przed ciężkim przebiegiem choroby'),
    #     (3, 'Uchronienie bliskich przed zachorowaniem/ciężkim przebiegiem choroby'),
    #     (4, 'Presja ze strony rodziny'),
    #     (5, 'Presja ze strony społeczeństwa'),
    #     (6, 'Było to wymagane w miejscu pracy'),
    #     (7, 'Możliwość wyjazdu za granicę'),
    #     (8, 'Inne powody (wymień jakie)'),
    # ])

    #Czy_uważasz,_że_przyjęcie_szczepionki_przeciw_COVID-19_przyniosło_ci_korzyści? = forms.ChoiceField(choices=[
    #     (1, 'Tak'),
    #     (2, 'Nie'),
    #     (3, 'Trudno powiedzieć'),
    # ]) 

    #Czy_doświadczyłeś_skutków_niepożądanych_przyjęcia_szczepionki?= forms.ChoiceField(choices=[
    #     (1, 'Tak'),
    #     (2, 'Nie'),
    #     (3, 'Nie pamiętam'),
    # ]) 

    #Jeśli_tak,_to_jakich? = forms.MultipleChoiceField(choices=[
    #     (1, 'Gorączka'),
    #     (2, 'Zmęczenie, złe samopoczucie'),
    #     (3, 'Ból głowy'),
    #     (4, 'Ból mięśni'),
    #     (5, 'Ból stawów'),
    #     (6, 'Dreszcze'),
    #     (7, 'Dolegliwości ze strony układu pokarmowego (biegunka, mdłości, ból brzucha)'),
    #     (8, 'Ból w miejscu wstrzyknięcia/opuchlizna/zaczerwienienie w miejscu wstrzyknięcia'),
    #     (9, 'Nadmierne pocenie się'),
    #     (10, 'Swędzenie skóry lub wysypka'),
    #     (11, 'Powiększone węzły chłonne'),
    #     (12, 'Uczucie omdlenia lub oszołomienia'),
    #     (13, 'Trudności z oddychaniem'),
    #     (14, 'Świszczący oddech'),
    #     (15, 'Opuchlizna twarzy i gardła'),
    #     (16, 'Przyspieszenie akcji serca'),
    #     (17, 'Inne, jakie? (pole do wpisania)'),
    # ])
	
    #Czy_doświadczone_skutki_uboczne_wpłynęły_na_twoją_decyzję_dotyczącą_przyjęcia_kolejnych_dawek_szczepionki? = forms.ChoiceField(choices=[
    #     (1, 'Tak'),
    #     (2, 'Nie'),
    # ]) 

    #Czy_doświadczone_skutki_uboczne_zmieniły_twój_stosunek_do_szczepień? = forms.ChoiceField(choices=[
    #     (1, 'Tak'),
    #     (2, 'Nie'),
    # ]) 

    #Czy_rekomendujesz_szczepienie_innym_mimo_doświadczonych_skutków_ubocznych? = forms.ChoiceField(choices=[
    #     (1, 'Tak'),
    #     (2, 'Nie'),
    # ]) 

     #11)Z_jakich_powodów_postanowiłaś/eś_się_nie_szczepić?  = forms.MultipleChoiceField(choices=[
    #     (1, 'Obawa przed NOP'),
    #     (1, 'Niepewność co do sposobu działania szczepionki'),
    #     (1, 'Niepewność co do składu szczepionki (możliwa zawartość szkodliwych substancji)'),
    #     (1, 'Preferencja nabycia odporności drogą naturalną (przechorowania COVID-19)'),
    #     (1, 'Brak zaufania do firm farmaceutycznych produkujących szczepionki'),
    #     (1, 'Rozmowa z rodziną/znajomymi'),
    #     (1, 'Presja ze strony rodziny/znajomych'),
    #     (1, 'Brak dostępności szczepionki'),
    #     (1, 'Inne, jakie (pole do wpisania)'),
    # ])

    #Czy_zaszczepiłaś/eś_swoje_dzieci_przeciwko_COVID-19?  = forms.ChoiceField(choices=[
    #     (1, 'Tak, szczepiłam/em'),
    #     (2, 'Nie, ale mam zamiar'),
    #     (3, 'Nie i nie mam zamiaru'),
    #     (4, 'Nie wiem'),
    # ])


    #Szczepienia przyszłe

    #Czy_przyjmiesz_kolejną_dawkę_szczepionki_przeciwko_COVID-19,_jeśli_takie_będą_zalecenia_lekarzy? = forms.ChoiceField(choices=[
    #     (1, 'Tak'),
    #     (2, 'Nie'),
    #     (3, 'Trudno powiedzieć'),
    # ]) 

    #Czy_w_przypadku_pojawienia_się_nowego_wirusa_byłabyś/byłbyś_skłonna/y_zaszczepić_się_od_razu_po_powstaniu_szczepionki? = forms.ChoiceField(choices=[
    #     (1, 'Tak'),
    #     (2, 'Nie'),
    #     (3, 'Trudno powiedzieć'),
    # ]) 

    #Czy_jesteś_skłonny_przyjmować_aktualnie_dostępne_i_zalecane_szczepionki_(np._szczepionki_przeciwko_grypie)? = forms.ChoiceField(choices=[
    #     (1, 'Tak'),
    #     (2, 'Nie'),
    #     (3, 'Trudno powiedzieć'),
    # ]) 

    #Jak_oceniasz_swój_stosunek_do_szczepień_(innych_niż_na_Covid) = forms.MultipleChoiceField(choices=[
    #     ('1', 'zdecydowanie negatywny'),
    #     ('2', 'raczej negatywny'),
    #     ('3', 'neutralny'),
    #     ('4', 'raczej pozytywny'),
    #      ('5', 'zdecydowanie pozytywny'),
    # ])

    #Metryczka
    
    # Wiek = forms.ChoiceField(choices=[
    #     (1, 'Poniżej 18'),
    #     (2, '18-29'),
    #     (3, '30-39'),
    #     (4, '40-49'),
    #     (5, '50-59'),
    #     (6, 'Powyżej 60'),
    # ])
      
     # Płeć = forms.ChoiceField(choices=[
    #     (1, 'Kobieta'),
    #     (2, 'Mężczyzna'),
    #     (3, 'Inna/nie chcę podawać'),
    # ])
     
     # Wykształcenie= forms.ChoiceField(choices=[
    #     (1, 'Podstawowe'),
    #     (2, 'Gimnazjalne'),
    #     (3, 'Średnie'),
    #     (4, 'Zasadnicze zawodowe'),
    #     (5, 'Wyższe'),
    # ]) 

     # Status zawodowy= forms.MultipleChoiceField(choices=[
    #     (1, 'Pracuję'),
    #     (2, 'Uczę się '),
    #     (3, 'Studiuję'),
    #     (3, 'Nie pracuję'),
    # ]) 

    # 	W jakim zawodzie pracujesz?= forms.ChoiceField(choices=[
    #     (1, 'Wpisz'),
    # ]) 


     #Miejsce zamieszkania = forms.ChoiceField(choices=[
    #     (1, 'Wieś'),
    #     (2, 'Miasto poniżej 100 tys.'),
    #     (3, 'Miasto 100-500 tys.'),
    #     (3, 'Miasto powyżej 500 tys.'),
    # ]) 
