from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Todo
from .serializers import TodoSerializer


class TodosView(APIView):

    def get(self, request):
       todos = Todo.objects.filter(user=request.user.id)
       serializer = TodoSerializer(todos, many=True)
       return Response(serializer.data)

    def post(self, request):
       serializer = TodoSerializer(data=request.data)
       data = serializer.data
       user = User.objects.get(id=data['user'])
       todo = Todo(user=user, description=data["description"], completed=False)
       request.data["id"] = todo.id
       todo.save()
       return Response(status=status.HTTP_201_CREATED)

    def put(self, request, todo_id):
       serializer = TodoSerializer(data=request.data)
       data = serializer.data
       description = data["description"]
       completed = data["completed"]
       todo = Todo(id=todo_id, user=request.user, description=description, completed=completed)
       todo.save()
       return Response(status=status.HTTP_202_ACCEPTED)

    def delete(self, request, todo_id):
       todo = Todo.objects.get(id=todo_id)
       todo.delete()
       return Response(status=status.HTTP_200_OK)

