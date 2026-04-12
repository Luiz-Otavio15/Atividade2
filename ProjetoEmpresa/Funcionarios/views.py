from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/painel.html'


def home(request):
    return render(request, 'usuarios/home.html')


@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')