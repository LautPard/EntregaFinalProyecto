"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from Zaunita.views import(  index,
                            about,
                            PublicacionList,
                            PublicacionDetail,
                            PublicacionCreate,
                            PublicacionUpdate, 
                            PublicacionDelete, 
                            SignUp,
                            Login,
                            Logout,
                            PerfilUpdate,
                            PerfilCreate,
                            CorreoCreate,
                            CorreoDelete,
                            CorreoList

                                )
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('publicacion/list', PublicacionList.as_view(), name="publicacion-list"),
    path('publicacion/<pk>/detail', PublicacionDetail.as_view(), name="publicacion-detail"),
    path('publicacion/create', PublicacionCreate.as_view(), name="publicacion-create"),
    path('publicacion/<pk>/update', PublicacionUpdate.as_view(), name="publicacion-update"),
    path('publicacion/<pk>/delete', PublicacionDelete.as_view(), name="publicacion-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('perfil/<pk>/update', PerfilUpdate.as_view(), name="perfil-update"),
    path('perfil/<pk>/create', PerfilCreate.as_view(), name="perfil-create"),
    path('correo/enviar', CorreoCreate.as_view(), name="correo-create"),
    path('correo/<pk>/delete', CorreoDelete.as_view(), name="correo-delete"),
    path('correo/list', CorreoList.as_view(), name="correo-list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)