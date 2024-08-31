from django.shortcuts import render
from django.shortcuts import render, redirect

from .forms import  PostModelForm


# Create your views here.
def inicio(request):
    pass
    return render(request, 'inicio.html')

def agregar_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostModelForm
    return render(request, 'agregar_post.html', {'form': form})
