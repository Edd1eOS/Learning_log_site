from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from .models import Topic,Entry

from .forms import TopicForm,EntryForm,Entry

from django.http import Http404
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html') ##告诉Django使用index.html这个模板来生成响应，而index.html这个模板位于learning_logs/templates/learning_logs/index.html，暂时还没有，需要前往创建
# Create your views here.

@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    # 检查主题的所有者是否是当前用户，如果不是，则返回404错误
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)#这一段的逻辑是：首先，根据用户输入的topic_id，从数据库中获取对应的topic对象。然后，根据这个topic对象，获取这个topic下的所有条目，并排序。最后，将这些数据传递给模板，并渲染成HTML页面。

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据：创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            #将新主题关联到用户，三行分别作用如下：
            #1.把表单数据转化为数据库可处理类型
            #2.用“当前请求发送者”赋值给“新主题的所有者”
            #3.永久储存进数据库
            return redirect('learning_logs:topics')#如果验证成功，就重定向到topics页面
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)#创建一个新表单

@login_required
def new_entry(request, topic_id):
    """在特定的主题下添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #未提交数据，创建一个空表单
        form = EntryForm()
    else:
        #POST提交数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        #POST提交数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

