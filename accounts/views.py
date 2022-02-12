from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from animals.models import Animal
from django.views.generic.detail import DetailView
from . forms import LoginForm, RegisterForm



class OwnerDetailView(DetailView):
    model = User
    template_name= 'owner_detail.html' 
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals'] = Animal.objects.filter(available = True, owner_id= self.kwargs['pk'])
        return context
    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) 

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Disable Account')

            else:
                messages.info(request, 'Check Your Usarname and Password')

    else:
        form = LoginForm() 
    return render(request, 'login.html', {'form':form})                                       


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created, You can LOGIN')
            return redirect('login')
                
    else:
        form = RegisterForm()   

    return render(request, 'register.html', {'form':form})                    


def user_logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def user_dashboard(request):
    current_user = request.user

    animals = current_user.animal_follower.all() 
    context = {
        'animals': animals
    }

    return render (request,'dashboard.html',context)


def follow_animal(request):
    animal_id = request.POST['animal_id']
    user_id = request.POST['user_id']
    animal = Animal.objects.get(id = animal_id)
    user = User.objects.get(id = user_id)
    animal.followers.add(user)
    return redirect('dashboard')