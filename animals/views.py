from multiprocessing import context
from django.shortcuts import render
from . models import Animal

# Create your views here.

def animal_list(request):
    animals = Animal.objects.all().order_by('-date')
    context = {'animals':animals}
    return render(request,'animals.html',context) 