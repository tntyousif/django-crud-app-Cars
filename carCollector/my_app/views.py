from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Modification, Filling
from .forms import FillingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    
    fillings = FillingForm()
    modifications = Modification.objects.all()
    
    return render(request, 'cars/detail.html', {
        'car': car,
        'fillings': fillings,
        'modification': modifications
    })

@login_required
def add_filling(request, car_id):
    form = FillingForm(request.POST)
    if form.is_valid():
        new_filling = form.save(commit=False)
        new_filling.car_id = car_id
        new_filling.save()
    return redirect('car-detail', car_id=car_id)

# CBVs for Car
class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['make', 'model', 'year']
    success_url = '/cars/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['make', 'model', 'year']

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'

# CBVs for Modification
class ModificationCreate(LoginRequiredMixin, CreateView):
    model = Modification
    fields = ['name', 'brand']
    success_url = '/modifications/'

class ModificationList(LoginRequiredMixin, ListView):
    model = Modification

class ModificationDetail(LoginRequiredMixin, DetailView):
    model = Modification

class ModificationUpdate(LoginRequiredMixin, UpdateView):
    model = Modification
    fields = ['name', 'brand']

class ModificationDelete(LoginRequiredMixin, DeleteView):
    model = Modification
    success_url = '/modifications/'

@login_required
def associate_modification(request, car_id, modification_id):
    Car.objects.get(id=car_id).modifications.add(modification_id)
    return redirect('car-detail', car_id=car_id)

@login_required
def remove_modification(request, car_id, modification_id):
    car = Car.objects.get(id=car_id)
    modification = Modification.objects.get(id=modification_id)
    car.modifications.remove(modification)
    return redirect('car-detail', car_id=car.id)