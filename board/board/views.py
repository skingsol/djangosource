from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.utils import timezone

"""
페이지 나누기
Paginator 클래스
Paginator(전체리스트, 페이지당 보여줄개수)

has_previous : 이전 페이지 유무
has_next : 다음 페이지 유무

previous_page_number : 이전 페이지 번호
next_page_number : 다음 페이지 번호
number : 현재 페이지 번호
page_range : 페이지 범위
"""


def index(request):
    # 질문 목록

    # 페이지 나누기 - 사용자가 요청한 페이지 가져오기
    # http://127.0.0.1:8000/board/?page=1
    # page = request.GET['page']
    page = request.GET.get("page", 1)

    # select * from question 와 같은 역활
    # question_list = Question.objects.all()

    # select * from question order by created_at desc 와 같은 역활
    question_list = Question.objects.order_by("-created_at")

    paginator = Paginator(question_list, 10)
    # pageinator 사용자가 요청한 페이지 정보 담기
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj}

    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    # qid 조회
    # select * from question where id=qid
    # get_object_or_404(), get(), filter()
    question = get_object_or_404(Question, id=qid)

    context = {"question": question}

    return render(request, "board/question_detail.html", context)


@login_required(login_url="users:login")
def question_create(request):
    """
    질문등록
    get - 비어있는 QuestionForm 보내기
    post - QuestionForm에 사용자 입력값 연결
    """
    if request.method == "POST":
        # 사용자 입력값 가져오기
        # subject = request.POST['subject']
        # content = request.POST['content']
        # 유효성 검사 코드
        # question = Question(subject=subject, content=content)
        # question.save()
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # request.user : 로그인 사용자
            question.save()
            return redirect("board:index")

    else:
        form = QuestionForm()
    return render(request, "board/question_create.html", {"form": form})


@login_required(login_url="users:login")
def question_edit(request, qid):
    """
    get : 수정할 질문을 보여주기
    post :질문 순정 => form에 질문 담아서 보내기
    post : 질문 수정
    """
    question = get_object_or_404(Question, id=qid)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            # 수정날짜 추가
            question = form.save(commit=False)
            question.modified_at = timezone.now()
            question.save()
            return redirect("board:detail", qid=qid)
    else:
        form = QuestionForm(instance=question)
    return render(request, "board/question_edit.html", {"form": form})


@login_required(login_url="users:login")
def question_delete(request, qid):
    """
    qid로 질문하기 => 삭제(delete())
    """
    question = get_object_or_404(Question, id=qid)
    question.delete()

    # 삭제 후 리스트로 이동
    return redirect("index")


####################### 답변
@login_required(login_url="users:login")
def answer_create(request, qid):
    """
    답변등록
    1) question 을 이용해 답변 등록
    question.answer_set.create()

    2) insert into answer (content,qid) values('답변',1)
    question = get_object_or_404(Question, id=qid)
    answer = Anser(question=question, content=request.POST[''])
    answer.save()
    """

    # question = get_object_or_404(Question, id=qid)
    # 1번 방식으로 할 경우 save() 명령어 안해도 됨
    # question.answer_set.create(content=request.POST["content"])

    # form 사용방식
    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # form.save() : commit 은 default 가 True 상태로 db 바로 반영
            answer = form.save(commit=False)
            # 어느 질문에 대한 답변인가?
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect("board:detail", qid=qid)
    else:
        form = AnswerForm()
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)


@login_required(login_url="users:login")
def answer_edit(request, aid):
    """
    get : 수정할 질문을 보여주기
    post :질문 순정 => form에 질문 담아서 보내기
    post : 질문 수정
    """
    answer = get_object_or_404(Answer, id=aid)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)

        if form.is_valid():
            # 수정날짜 추가
            answer = form.save(commit=False)
            answer.modified_at = timezone.now()
            answer.save()
            return redirect("board:detail", qid=answer.question_id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, "board/answer_edit.html", {"form": form})


@login_required(login_url="users:login")
def answer_delete(request, aid):
    """
    qid로 질문하기 => 삭제(delete())
    """
    answer = get_object_or_404(Answer, id=aid)
    answer.delete()

    # 삭제 후 리스트로 이동
    return redirect("board:detail", qid=answer.question_id)
