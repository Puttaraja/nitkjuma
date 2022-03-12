from django.urls import URLPattern, path, include
from . import views

urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('categories/<int:cat_id>/',views.items,name='items'),
    path('categories/<int:cat_id>/<int:item_id>/',views.item,name='item'),
    path('upload/', views.upload, name='upload'),
]