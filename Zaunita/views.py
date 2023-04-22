from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Zaunita.models import Publicacion, Perfil, Correo
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    context = {
        "publicaciones": Publicacion.objects.all()
    }
    
    return render(request, "Zaunita/index.html", context)

def about(request):
    return render(request, "Zaunita/about.html")


class PublicacionList(ListView):
    model = Publicacion
    context_object_name = "publicaciones"
    

class PublicacionDetail(DetailView):
    model = Publicacion
    

class PublicacionCreate(LoginRequiredMixin, CreateView):
    model = Publicacion
    success_url = reverse_lazy("publicacion-list")
    fields = '__all__'

class PublicacionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publicacion
    success_url = reverse_lazy("publicacion-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Publicacion.objects.filter(gymrat=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, 'Zaunita/not_found.html')

class PublicacionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publicacion
    success_url = reverse_lazy("publicacion-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Publicacion.objects.filter(gymrat=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, 'Zaunita/not_found.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    next_page = reverse_lazy("index")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class PerfilUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Perfil
    fields = "__all__"
    success_url = reverse_lazy("publicacion-list")

    def test_func(self):
        return self.request.user.is_authenticated
    def handle_no_permission(self):
        return render(self.request, 'Zaunita/not_found.html')

class PerfilCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Perfil
    fields = "__all__"
    success_url = reverse_lazy("publicacion-list")

    def test_func(self):
        return self.request.user.is_authenticated
    def handle_no_permission(self):
        return render(self.request, 'Zaunita/not_found.html')

class CorreoCreate(CreateView):
    model = Correo
    fields = '__all__'
    success_url = reverse_lazy("correo-list")

class CorreoList(ListView):
    model = Correo
    context_object_name = "correos"

    def get_queryset(self):
        return Correo.objects.filter(destinatario=self.request.user.id).all()
    
class CorreoDelete(DeleteView):
    model = Correo
    success_url = reverse_lazy("correo-list")