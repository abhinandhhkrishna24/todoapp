from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

# Create your views here.


class TodoItemList(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemCreate(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemUpdate(generics.RetrieveUpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemComplete(generics.RetrieveUpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    lookup_field = 'pk'

    def put(self, request, pk):
        todo_item = get_object_or_404(self.queryset, pk=pk)
        todo_item.completed = True
        todo_item.save()
        serializer = self.serializer_class(todo_item)
        return Response(serializer.data)

class TodoItemDelete(generics.DestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
