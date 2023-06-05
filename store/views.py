from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Game
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:login')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store:home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('store:login')

@login_required
def home(request):
    games = Game.objects.all()
    return render(request, 'store/home.html', {'games': games})

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_games(request):
    games = Game.objects.all()
    return render(request, 'store/home.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'store/game.html', {'game': game})

def checkout(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        game_name = request.POST.get('game_name')
        game_price = request.POST.get('game_price')
        game_image = request.POST.get('game_image')

        context = {
            'game_id': game_id,
            'game_name': game_name,
            'game_price': game_price,
            'game_image': game_image
        }
        return render(request, 'store/checkout.html', context)

    return redirect('store:cart')

def payment(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')

        # Process payment logic here

        return render(request, 'store/payment_success.html')

    return redirect('store:cart')

def payment_success(request):
    return render(request, 'store/payment_success.html')

def e_news(request):
    return render(request, 'store/e_news.html')