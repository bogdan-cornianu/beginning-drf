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

   def put(self, request):
       serializer = TodoSerializer(data=request.data)
       data = serializer.data
       description = data["description"]
       completed = data["completed"]
       todo = Todo(id=id, user=request.user, description=description, completed=completed)
       todo.save()

   def delete(self, request):
       todo = Todo.objects.get(id=id)
       todo.delete()

