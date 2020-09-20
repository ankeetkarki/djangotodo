from django.urls import path
from . import views


urlpatterns = [
	path('todos/', views.todopage, name = 'todo-page'),
	path('addtodo/', views.addtodo, name = 'add-page')
]