from django.shortcuts import render
from django.contrib.auth.models import User
from animals.models import Animal
from django.views.generic.detail import DetailView



class TeacherDetailView(DetailView):
    model = User
    template_name= 'owner_detail.html' 
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals'] = Animal.objects.filter(available = True, owner_id= self.kwargs['pk'])
        return context
    




def user_detail(request, pk):
    user = User.objects.get(id = pk)
    animals = user.animal_set.all()


    context = {'user': user,'animals':animals}
    return render(request, 'owner_detail.html', context)