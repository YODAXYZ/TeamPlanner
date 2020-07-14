from django import forms
from columns.models import Column


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ("column_title",)
