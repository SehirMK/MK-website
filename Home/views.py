from django.http import HttpResponseRedirect
from django.shortcuts import render
#from django.http import HttpResponse
from . import forms
#from Home.models import User
from Home.forms import FormName

# Create your views here.

def index(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'Home/index.html', {'form':form})

