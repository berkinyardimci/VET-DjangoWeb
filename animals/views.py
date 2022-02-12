from multiprocessing import context
from urllib import request
from django.shortcuts import get_object_or_404, render
from . models import Animal, Type, Genus
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.



def animal_list(request, type_slug=None, genus_slug=None):
    type_page = None
    genus_page = None
    types = Type.objects.all()
    genus = Genus.objects.all() 

    if type_slug != None:
        type_page = get_object_or_404(Type, slug= type_slug)
        animals = Animal.objects.filter(available = True, type = type_page)

    elif genus_slug != None:
        genus_page = get_object_or_404(Genus, slug= genus_slug)
        animals = Animal.objects.filter(available = True, genus = genus_page)

    else:
        animals = Animal.objects.all().order_by('-created')

    context = {'animals':animals,'types':types,'genus':genus}
    return render(request,'animals.html',context) 


def animal_detail(request, type_slug, animal_id):
    animal = Animal.objects.get(type__slug = type_slug, id = animal_id )
    types = Type.objects.all()
    context = {'animal': animal,'types':types}

    return render(request,'animal_detail.html',context) 


def search(request):
    animals = Animal.objects.filter(
        Q(name__contains=request.GET['search']) |
        Q(genus__name__icontains= request.GET['search']) |
        Q(type__name__icontains=request.GET['search']) 
        )     

    types = Type.objects.all()
    genus = Genus.objects.all()

    context = {'animals':animals,'types':types,'genus':genus}
    return render(request,'animals.html',context)     

# def animal_list(request):
#     animals = Animal.objects.all().order_by('-created')
#     types = Type.objects.all()
#     genus = Genus.objects.all()
#     context = {'animals':animals,'types':types,'genus':genus}

#     return render(request,'animals.html',context) 




# def type_list(request,type_slug):
#     animals = Animal.objects.all().filter(type__slug = type_slug)
#     types = Type.objects.all()
#     genus = Genus.objects.all()
#     context = {'animals': animals, 'types':types,'genus':genus}

#     return render(request,'animals.html',context)     


# def genus_list(request,genus_slug):
#     animals = Animal.objects.all().filter(genus__slug = genus_slug)
#     types = Type.objects.all()
#     genus = Genus.objects.all()
#     context = {'animals': animals, 'types':types,'genus':genus}

#     return render(request,'animals.html',context)     
