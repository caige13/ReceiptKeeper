
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import redirect
from .models import textEditor
fill_out = True
@login_required(login_url='/accounts/login/')
def create_job(request):
    template = loader.get_template('Job/Add.html')
    global fill_out
    print("request:::, ", request.GET)
    if 'fill_out' in request.GET:
        fill_out = True
    else:
        fill_out = False
    context = {'fill_out': fill_out}
    return HttpResponse(template.render(context, request))
