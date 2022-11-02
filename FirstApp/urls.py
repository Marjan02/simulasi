from django.contrib import admin
from django.urls import path, include
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Home Page')

# def room(request):
#     return HttpResponse('ROOM')

urlpatterns = [
    path('admin/', admin.site.urls), # routes ademin
    path('', include('base.urls')), # routes biasa
    path('api/', include('api.urls')) # routes api
]
