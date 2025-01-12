from django.shortcuts import render
from vet.models import PetOwner
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView, View  # Asegúrate de importar TemplateView correctamente

# Create your views here.
def list_pet_owners(request):
    """"List owners"""
    owners = PetOwner.objects.all()
    context = {"owners": owners}
    template = loader.get_template("vet/owners/list.html")
    return HttpResponse(template.render(context, request))


class OwnersList(TemplateView):
    template_name = "vet/owners/list.html"

    def get_context_data(self, **kwargs):  # Corregido 'sef' por 'self'
        context = super().get_context_data(**kwargs)
        context['owners'] = PetOwner.objects.all()
        return context


class Test(View):
    def get(self, request):
        return HttpResponse("Hello world from a class generic view")
