from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView
from vet.models import PetOwner, Pet
from django.urls import reverse_lazy
from .forms import OwnerForm, PetForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

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
    template_name = "vet/pet/list_pet.html"
    context_object_name = "pets"

class PetDetail(DetailView):
    """Render a detailed view of a specific pet based on its pk."""
    model = Pet
    template_name = "vet/pet/detail_pet.html"
    context_object_name = "pet"

class OwnerDetail(LoginRequiredMixin, DetailView):
    """Render a detailed view of a specific pet owner based on their pk."""
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"

class Test(View):
    """A simple test view."""
    def get(self, request):
        return HttpResponse("Hello world from a class-based generic view")


class OwnersCreate(CreateView):
    """"View used to create a PetOwner."""
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")

class PetCreate(CreateView):
    """"View used to create a Pet."""
    model = Pet
    template_name = "vet/pet/create_pet.html"
    form_class = PetForm
    success_url = reverse_lazy("vet:pet_list")


class OwnersUpdate(PermissionRequiredMixin, UpdateView):
    """"View used to create a PetOwner."""
    permission_required = "vet.change_petowner"
    raise_exception = False
    login_url = "/admin/login"

    redirect_field_name = "next"
    model = PetOwner
    template_name = "vet/owners/update.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")

class PetUpdate(UpdateView):
    """"View used to create a PetOwner."""
    model = Pet
    template_name = "vet/pet/update_pet.html"
    form_class = PetForm
    success_url = reverse_lazy("vet:pet_list")