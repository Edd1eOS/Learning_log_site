from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic#模型
        fields = ['text']#添加字段
        labels = {'text': ''}#添加标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}