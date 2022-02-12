from django.views.generic import TemplateView
from animals.models import Animal
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from pages.forms import ContactForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals'] = Animal.objects.filter(available=True).order_by('-created')[:2]
        context['total_animals'] = Animal.objects.filter(available=True).count()
        context['total_user'] = User.objects.all().count
        return context

class AboutView(TemplateView):
    template_name= 'about.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm