from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.integration_type import IntegrationType
from users.models import PerfilUsuario

# Transbank credentials (replace with your own in production)
commerce_code = "597055555532"
api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"

Transaction.commerce_code = commerce_code
Transaction.api_key = api_key
Transaction.integration_type = IntegrationType.TEST

@login_required
def add_money(request):
    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        if amount <= 0:
            return render(request, "add_money.html", {"error": "El monto debe ser mayor a 0."})

        tx = Transaction()
        response = tx.create(
            buy_order=f"order-{request.user.id}-{PerfilUsuario.objects.count()}",
            session_id=str(request.user.id),
            amount=amount,
            return_url="http://127.0.0.1:8000/add-money-confirmation/"
        )

        # Redirect to Transbank payment page
        return redirect(response["url"] + "?token_ws=" + response["token"])

    return render(request, "add_money.html")


@login_required
def add_money_confirmation(request):
    token = request.GET.get("token_ws")
    tx = Transaction()
    response = tx.commit(token)

    if response["status"] == "AUTHORIZED":
        # Update the user's saldo
        perfil = request.user.perfilusuario
        perfil.saldo += response["amount"]
        perfil.save()

        return render(request, "add_money_confirmation.html", {"success": True, "amount": response["amount"]})
    else:
        return render(request, "add_money_confirmation.html", {"success": False})