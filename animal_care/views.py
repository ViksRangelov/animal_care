from django.shortcuts import render, redirect

from animal_care.forms import AnimalForm
from animal_care.models import Animal


def index(request):
    animals = Animal.objects.all()
    cured_animals = Animal.objects.all().filter(is_cured=True)

    context = {
        'animals': animals,
        'cured_animals': cured_animals
    }
    return render(request, 'index.html', context)


def create_animal(request):
    if request.method == 'GET':
        form = AnimalForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = AnimalForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect('index')


def edit_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    if request.method == 'GET':
        form = AnimalForm(instance=animal)
        return render(request, 'edit.html', {'form': form})
    else:
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect('index')


def delete_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    if request.method == 'GET':
        form = AnimalForm(instance=animal)
        return render(request, 'delete.html', {'form': form})
    else:
        animal.delete()
        return redirect('index')


def details(request, pk):
    animal = Animal.objects.get(pk=pk)
    form = AnimalForm(instance=animal)

    return render(request, 'details.html', {'form': form})


def cure(request, pk):
    animals = Animal.objects.all()
    animal = Animal.objects.get(pk=pk)
    animal.is_cured = True
    cured_animals = Animal.objects.all().filter(is_cured=True)
    context = {
        'animals': animals,
        'cured_animals': cured_animals
    }
    return redirect(request, 'index.html', context)
