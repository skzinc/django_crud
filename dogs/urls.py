from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/update/<int:id>', views.update, name="update"),
    path('add/', views.add, name="add"),
    path('create/', views.create, name="create"),
]
