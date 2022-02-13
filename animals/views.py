from django.shortcuts import get_object_or_404, render,redirect
from . models import Animal, Type, Genus
from django.db.models import Q
from django.contrib.auth.models import User
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
            image = request.POST.get('image'),
        )
        messages.info(request, 'Başarılıııı')
        return redirect('animals')

        # else:
        #     messages.info(request, 'Check Your Usarname and Password')
        #     return redirect('index')

    else:
        form = AnimalForm()
        context = {'form':form}
        return render (request, 'create_animal.html', context)


# @login_required(login_url='login')
# def create_animal(request):
#     if request.method == 'POST':
#         form = AnimalForm(request.POST, request.FILES)
#         if form.is_valid():
#             current_user = request.user
#             post = Animal()
#             post.owner_id = current_user.id
#             post.name = form.cleaned_data['name']
#             post.type.name = form.cleaned_data['type']
#             post.genus.name = form.cleaned_data['genus']
#             post.age = form.cleaned_data['age']
#             post.description = form.cleaned_data['description']
#             post.image = form.cleaned_data['image']
#             post.save()
#             messages.success(request, 'Ekleme basarili')
#             return redirect('animals')
#         else:
#             messages.success(request, 'Content Form Error:' + str(form.errors))
#             return redirect('index')
#     else:

#         form = AnimalForm()
#         context = {

#             'form': form,

#         }
#         return render(request, 'create_animal.html', context)