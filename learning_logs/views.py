from django.shortcuts import render

from .models import Topic

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html') ##告诉Django使用index.html这个模板来生成响应，而index.html这个模板位于learning_logs/templates/learning_logs/index.html，暂时还没有，需要前往创建
# Create your views here.

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)