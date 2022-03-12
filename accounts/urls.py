from django.urls import URLPattern, path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup ,name='signup'),
    path('profile/', views.profile ,name='profile'),
]