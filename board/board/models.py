from django.db import models

# Question 테이블
# 번호(자동생성), 제목, 내용, 작성날짜, 수정날짜
class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    # auto_now_add : insert 시 자동으로 시간/날짜 삽입
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)

    def __str__(self) -> str:
        return self.subject
    


# Answer 테이블
# 번호(자동생성), 외래키 제약, 내용, 작성날짜, 수정날짜
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)