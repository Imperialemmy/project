from django.urls import path
from . import views 

# urlpatterns = [
#     path('login/',views.index, name = 'homepage'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name = 'register'),
    path('home/', views.home, name = 'home' )
]
