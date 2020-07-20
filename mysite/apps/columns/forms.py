from django import forms
from columns.models import Column
from tasks.models import Task


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ("column_title",)


# from django import forms
# from columns.models import Column
# from tasks.models import Task
#
#
# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ("author", "title", "pub_date", "lead_time",)
