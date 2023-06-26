from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('all-games/', views.all_games, name='all_games'),
    path('item/<int:game_id>/', views.game_detail, name='game_detail'),
    # path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('e_news/', views.e_news, name='e_news'),

]
