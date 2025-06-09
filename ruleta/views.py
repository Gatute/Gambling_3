import random
from django.shortcuts import render
from .models import Apuesta
from users.models import PerfilUsuario
# Create your views here.
def ruleta_page(request):
    return render(request, 'Ruleta.html')
def ruleta_page2(request):
    return render(request, 'Ruleta2.html')

def jugar_ruleta(request):
    if request.method == "POST":
        usuario = request.user.PerfilUsuario
        monto = float(request.POST["monto"])

        if usuario.saldo < monto:
            return render(request, "TmteRuleta.html", {"error": "Saldo insuficiente"})

        resultado = random.choice(["rojo", "negro", "verde"])
        ganancia = 0

        if resultado == "rojo":
            ganancia = monto * 2 
        elif resultado == "verde":
            ganancia = monto * 10 

        usuario.saldo += ganancia - monto
        usuario.save()

        Apuesta.objects.create(usuario=usuario, monto=monto, resultado=resultado)

        return render(request, "TmteRuleta.html", {"resultado": resultado, "ganancia": ganancia})

    return render(request, "TmteRuleta.html")