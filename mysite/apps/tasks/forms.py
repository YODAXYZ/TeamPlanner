from django import forms
from tasks.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "comment_text",)
