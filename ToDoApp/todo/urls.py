from django.urls import path
from .views import (
    TodoItemList,
    TodoItemCreate,
    TodoItemUpdate,
    TodoItemComplete,
    TodoItemDelete,
)



urlpatterns = [
    path('todos/', TodoItemList.as_view(), name='todo-list'),
    path('todos/create/', TodoItemCreate.as_view(), name='todo-create'),
    path('todos/update/<int:pk>/', TodoItemUpdate.as_view(), name='todo-update'),
    path('todos/complete/<int:pk>/', TodoItemComplete.as_view(), name='todo-complete'),
    path('todos/delete/<int:pk>/', TodoItemDelete.as_view(), name='todo-delete'),
]