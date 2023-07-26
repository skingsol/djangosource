from django import forms
# 장고에서 제공하는 User 생성폼과 모델 가져오기
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    """
    - 상속받는Form 관계
    forms.ModelForm
        |
    BaseUserCreationForm : username, password1, password2
        |
    UserCreationForm
        |
    UserForm : User 모든 필드 + 상속

    UserCreationForm 클래스를 상속받는 Form 정의
    """
    
    # 부모가 넘겨주는 email 은 필수 입력 요소가 아님
    # 필수 입력 요소로 만들기 위해 사용
    email = forms.EmailField(label = "이메일")

    class Meta:
        model = User
        # fields = "__all__" + 상속
        fields = ["username", "email"] # + 상속 (password1, password2)