from django.urls import path
from .views import TodosApiView

urlpatterns = [
    # 클래스로 작성된 뷰 사용시 _as_view() 무조건 사용
    path("", TodosApiView.as_view(), name="todo"),
]
