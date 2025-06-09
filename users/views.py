from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def registro(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register.html",{"form":form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Matches the 'name' attribute in your form
        password = request.POST.get('password')  # Matches the 'name' attribute in your form
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Replace 'home' with your desired redirect URL
        else:
            return render(request, 'registration/login.html', {'errors': True})
    return render(request, 'registration/login.html')