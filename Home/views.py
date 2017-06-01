from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation success!')
            print('Name:' + form.cleaned_data['name'])
            print('Email:' + form.cleaned_data['email'])

    return render(request, 'Home/index.html', {'form':form})

