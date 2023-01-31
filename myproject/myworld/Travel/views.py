from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Travel

def members(request):
    mymembers = Travel.objects.all().values()
    context = {
    'mymembers': mymembers,
    }
    return render(request, 'Members.html', context)

def details(request, id):
    member = Travel.objects.get(id=id)
    context = {
    'member': member,
  }
    return render(request, 'details.html', context)

def main(request):
    return render(request, 'main.html')

def testing(request):
    template = loader.get_template('template.html')
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))