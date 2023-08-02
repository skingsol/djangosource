from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__" # 모델에 있는 모든 필드 사용
        # exclude = ["created_at", "modified_at"]
        fields = ["subject", "content", "image"]
