from django.views.generic import TemplateView 
from django.shortcuts import render 
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Bienvenidos a mi sitio de palabras") 

class IndexPageView(TemplateView): 
    template_name = "index.html" 


class PalindromoPageView(TemplateView): 
    template_name = "palindromo.html" 


def esPalindromo(request,name):

    name = name.replace(" ", "")
    nel=name

    context = {'name' : name} 
    if  str(nel) == str(name)[::-1]:
        return render(request, 'palindromoA.html', context)
    else:    
        return render(request, 'palindromoB.html', context)
    

