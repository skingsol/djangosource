from django.db import models

class Todo(models.Model):
    """
    제목 : text => CharField
    설명 : text => TextField
    작성날짜 : 시간/날짜
    완료여부 : True/False 
    중요여부 : True/False
    """
    title = models.CharField(max_length=50)
    description = models.TextField()
    # DateTimeField 옵션
    # auto_now_add : 처음 입력시 날짜/시간으로 셋팅 (insert시에만)
    # auto_now : 수정할때마다 계속 시간과 날짜가 자동 업데이트 (update시에만)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
