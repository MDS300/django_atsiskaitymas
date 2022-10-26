from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .models import Klientas, Darbuotojas, Darbas, Projektas, Saskaita
from django.views import generic
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


def index(request):
    context = {
        'kiek_klientu': Klientas.objects.all().count(),
        'kiek_darbuotoju': Darbuotojas.objects.all().count(),
        'kiek_darbu': Darbas.objects.all().count(),
        'kiek_projektu': Projektas.objects.all().count(),
    }

    return render(request, 'index.html', context=context)


def projektai(request):
    paginator = Paginator(Projektas.objects.all(), 3)
    page_number = request.GET.get('page')
    puslapiuoti_projektai = paginator.get_page(page_number)
    context = {
        'visi_projektai': puslapiuoti_projektai,
    }

    return render(request, 'projektai.html', context=context)


def projektas(request, pavadinimas):
    context = {
        'vienas_projektas': get_object_or_404(Projektas, pk=pavadinimas),
        'darbuotojai': Darbuotojas.objects.all(),
        'darbai': Darbas.objects.all(),

    }
    return render(request, 'projektas.html', context=context)

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


class ProjektasListView(LoginRequiredMixin, generic.ListView):
    model = Projektas
    template_name = 'priskirti_projektai.html'
    context_object_name = 'priskirti_projektai'

    def get_queryset(self):
        return Projektas.objects.filter(atsakingasis=self.request.user)

