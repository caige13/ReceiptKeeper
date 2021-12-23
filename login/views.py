from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.template import loader
from django.shortcuts import redirect

def login_view(request):
    template = loader.get_template('Registration/login.html')

    if request.user.is_authenticated:
        logout(request)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if "next" in request.GET:
                return redirect(request.GET["next"])
            return redirect("home")
        else:
            messages.error(request, "The Username and/or Password are incorrect.")

    context = {}
    return HttpResponse(template.render(context, request))