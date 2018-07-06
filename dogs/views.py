from django.shortcuts import render, redirect
from .models import Dogs

def index(request):
    dogs = Dogs.objects.all()

    context = {
        'dogs':dogs
    }
    return render(request, 'index.html', context)

def add(request):
    return render(request, 'add.html')

def create(request):

        if (request.method == 'POST'):
            name = request.POST['name']
            breed = request.POST['breed']

            dog = Dogs(name=name, breed=breed)
            dog.save()
            return redirect('/')
        else:
            return render(request, 'add.html')

def edit(request, id):
    dog = Dogs.objects.get(id=id)
    context={'dog':dog}
    return render(request, 'edit.html', context)

def update(request, id):
    dog = Dogs.objects.get(id=id)
    dog.name = request.POST.get('name')
    dog.breed = request.POST['breed']
    dog.save()
    return redirect('/')

def delete(request, id):
    dog = Dogs.objects.get(id=id)
    dog.delete()


    return redirect('/')
