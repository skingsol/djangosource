from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


class TodosApiView(APIView):
    def get(self, request):
        # complete 가 false 인 전체 todo 조회
        todos = Todo.objects.filter(complete=False)
        # 조회된 전체 todo를 TodoSerializer로 변환
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 위 코드는 아래 코드 대신 사용
# def todo_list(request):
#     if request.method == "GET":
#         todos = Todo.objects.filter(complete=False)
#         return render(request, "템플릿 파일명", {todos: todos})
