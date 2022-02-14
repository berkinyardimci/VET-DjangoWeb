from django.shortcuts import get_object_or_404, render,redirect
from . models import Animal, Type, Genus
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import AnimalForm
from django.contrib import messages

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
    current_user = request.user
    animal = Animal.objects.get(type__slug = type_slug, id = animal_id )
    animals = Animal.objects.all().order_by('-created')
    types = Type.objects.all()
    genus = Genus.objects.all()   

    if current_user.is_authenticated:
        followed_animals = current_user.animal_follower.all()  

    else:
        followed_animals= animals                

    context = {'animal': animal,'followed_animals': followed_animals,'types':types,'genus':genus}
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


@login_required(login_url='login')
def create_animal(request):
    form = AnimalForm(request.POST, request.FILES)
    types = Type.objects.all()
    genus = Genus.objects.all()

    if request.method == 'POST':
        type_name = request.POST.get('type')
        genus_name = request.POST.get('genus')
        type, created = Type.objects.get_or_create(name = type_name)
        genus, created = Genus.objects.get_or_create(name = genus_name)

        Animal.objects.create(
            owner = request.user,
            type = type ,
            genus = genus ,
            name = request.POST.get('name'),
            age = request.POST.get('age'),
            description = request.POST.get('description'),
            image = request.FILES.get('image'),
        )
        
        return redirect('animals')


    else:
        form = AnimalForm()
        context = {'form':form}
        return render (request, 'create_animal.html', context)

@login_required(login_url='login')
def update_animal(request, animal_id, type_slug):
    animal = Animal.objects.get(id = animal_id, type__slug = type_slug)
    form = AnimalForm(request.POST, request.FILES, instance=animal)
    types = Type.objects.all()
    genus = Genus.objects.all()    

    if request.user != animal.owner:
        return messages.error('Your are not allowed here !!')


    if request.method == 'POST':
        type_name = request.POST.get('type')
        genus_name = request.POST.get('genus')
        types, created = Type.objects.get_or_create(name = type_name)
        genus, created = Genus.objects.get_or_create(name = genus_name)

        animal.name = request.POST.get('name')
        animal.type = types
        animal.genus = genus        
        animal.description = request.POST.get('description')
        animal.age = request.POST.get('age')
        animal.image = request.FILES.get('image')
        animal.save()
        return redirect('index')  

    context = {'form': form,'types':types,'genus':genus }
    return render(request, 'update_animal.html', context)    

def delete_animal(request, animal_id, type_slug):
    animal = Animal.objects.get(id = animal_id, type__slug = type_slug)
    
    if request.method == 'POST':
        animal.delete()
        return redirect('animals')

    return render(request, 'delete.html', {'obj':animal})      