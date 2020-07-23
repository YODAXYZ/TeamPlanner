from django import forms
from .models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("board_title",)


class UserInvitationForm(forms.Form):
    user_id = forms.IntegerField(label='ID of the user you want to invite')
