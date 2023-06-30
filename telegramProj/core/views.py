from django.shortcuts import render, redirect
from django.views import View
from .forms import InscricaoForm
from django.contrib import messages
from .models import *
from django.http import JsonResponse


def check_unique_email(request):
    email = request.GET.get('email', '')
    is_unique = not Inscricoes.objects.filter(email=email).exists()
    return JsonResponse({'is_unique': is_unique})

def check_unique_phone(request):
    phone = request.GET.get('phone', '')
    is_unique = not Inscricoes.objects.filter(phone=phone).exists()
    return JsonResponse({'is_unique': is_unique})

class HomeView(View):
    def post(self, request):
        inscricao_form = InscricaoForm(request.POST)
        if inscricao_form.is_valid():
            inscricao_form.save()
            messages.success(request, 'Inscrição feita com sucesso!')
            return redirect('HomeView')  # Replace 'index' with the appropriate URL name for your index page
        else:
            messages.error(request, 'Erro ao enviar inscrição.\n Verifique os dados e tente novamente.\n Não se pode')
            return render(request, 'index.html', {'inscricao_form': inscricao_form})

    def get(self, request):
        inscricao_form = InscricaoForm()
        numero = len(Inscricoes.objects.all())

        context = {
            'n' : numero,
            'inscricao_form' : inscricao_form
        }
        return render(request, 'index.html',context)
