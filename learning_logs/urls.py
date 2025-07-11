from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #show all topics
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),#把topic_id作为参数传递给topic()，让Django知道要显示哪个主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),#用于添加新主题的页面
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
]   
