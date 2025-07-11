from django.shortcuts import render,redirect

from .models import Topic

from .forms import TopicForm,EntryForm,Entry
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html') ##告诉Django使用index.html这个模板来生成响应，而index.html这个模板位于learning_logs/templates/learning_logs/index.html，暂时还没有，需要前往创建
# Create your views here.

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)#这一段的逻辑是：首先，根据用户输入的topic_id，从数据库中获取对应的topic对象。然后，根据这个topic对象，获取这个topic下的所有条目，并排序。最后，将这些数据传递给模板，并渲染成HTML页面。

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据：创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')#如果验证成功，就重定向到topics页面
        
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)#创建一个新表单

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

def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

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

