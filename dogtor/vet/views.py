from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from vet.models import PetOwner, Pet
# Create your views here.
def list_pet_owners(request):
    """"List owners"""
    owners = PetOwner.objects.all()
    context = {"owners": owners}
    template = loader.get_template("vet/owners/list.html")
    return HttpResponse(template.render(context, request))


# class OwnersList(TemplateView):
#     template_name = "vet/owners/list.html"

#     def get_context_data(self, **kwargs):  # Corregido 'sef' por 'self'
#         context = super().get_context_data(**kwargs)
#         context['owners'] = PetOwner.objects.all()
#         return context


class OwnersList(ListView):
    """Render all Pet Owners."""
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"

class PetList(ListView):
    """Render all Pets."""
    model = Pet
    template_name = "vet/owners/list_pet.html"
    context_object_name = "pets"

class PetDetail(DetailView):
    """Render a detailed view of a specific pet based on its pk."""
    model = Pet
    template_name = "vet/owners/detail_pet.html"
    context_object_name = "pet"

class OwnerDetail(DetailView):
    """Render a detailed view of a specific pet owner based on their pk."""
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"

class Test(View):
    """A simple test view."""
    def get(self, request):
        return HttpResponse("Hello world from a class-based generic view")
