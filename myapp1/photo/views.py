from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Photo
from .forms import PhotoForm

"""
render(request객체,템플릿이름)

템플릿을 저장하는 폴더 기본값 : 앱 안의 templates 

"""


def photo_list(request):
    # 단순 문자열 화면에 표시
    # return HttpResponse("Hello Photo")

    # 템플릿 페이지 화면에 보여주기
    # return render(request,"photo_list.html")

    # 템플릿 + DB 내용 보여주기
    # Photo.objects.all() : select * from photo
    photos = Photo.objects.all()
    return render(request, "photo_list.html", {"photos": photos})


def photo_detail(request, id):
    # get_object_or_404(Photo, id=id) : id를 이용해서 찾은 후 찾은 정보를
    # Photo 객체에 담아주기, 찾는 데이터가 없다면 404 반환
    photo = get_object_or_404(Photo, id=id)
    return render(request, "photo_detail.html", {"photo": photo})


# def photo_post(request):
#     """
#     request 객체의 method 방식에 따라서 처리 방법 다르게 작성
#     """
#     if request.method == "POST":
#         title = request.POST["title"]
#         author = request.POST["author"]
#         image = request.POST["image"]
#         description = request.POST["description"]
#         price = request.POST["price"]
#         # print(title, author, image, description, price)

#         # db 작업 : 삽입할 객체 생성
#         photo = Photo(
#             title=title,
#             author=author,
#             image=image,
#             description=description,
#             price=price,
#         )
#         # 생성된 객체 저장(db에 insert 작업 실행)
#         photo.save()
#         # 목록 페이지로 이동
#         return redirect("photo_list")

#     return render(request, "photo_post.html")


def photo_post(request):
    """
    request 객체의 method 방식에 따라서 처리 방법 다르게 작성
    """
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():  # table 생성 규칙에 맞는지 확인
            form.save()  # 폼은 모델과 연결된 상황이므로 바로 insert 작업 이루어짐
            return redirect("photo_list")
    else:
        form = PhotoForm()

    return render(request, "photo_post.html", {"form": form})


def photo_edit(request, id):
    photo = get_object_or_404(Photo, id=id)

    if request.method == "POST":
        # POST로 넘어오는 값도 PhotoForm에 담겨져 있는 상황
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():  # table 생성 규칙에 맞는지 확인
            form.save()
            return redirect("photo_detail", id=photo.id)
    else:
        # 위에서 찾은 db 데이터를 폼에 담아서 보내기
        form = PhotoForm(instance=photo)

    return render(request, "photo_edit.html", {"form": form})


# 모델폼을 사용하지 않는 방식
# def photo_edit(request, id):
#     photo = get_object_or_404(Photo, id=id)

#     if request.method == "POST":
#         price = request.POST["price"]

#         photo.price = price
#         photo.save()  # update/insert
#         # 상세보기 이동 /photo/1
#         # return redirect("/photo/{}/".format(id))
#         return redirect("photo_detail", id=photo.id)

#     return render(request, "photo_edit.html", {"photo": photo})


def photo_remove(reqeust, id):
    """
    삭제 후 목록보기
    """
    # 삭제할 대상 찾기
    photo = get_object_or_404(Photo, id=id)
    photo.delete()  # delete from

    return redirect("photo_list")
