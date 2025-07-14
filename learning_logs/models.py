from django.db import models
from django.contrib.auth.models import User

#为学习笔记项目创建的模型
class Topic(models.Model):#继承模型类model.Model
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)#简单来说就是一个外键字段，关联auth.User模型，这里的一对多关系是：一个用户可以有多个主题，一个主题只能有一个用户，也就是一个entry只属于一个user。

    def __str__(self):
        return self.text

#以上是topic类，用于存储用户的学习板块主题

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...'
    text
#以上是entry类，用于存储用户学习板块的详细内容 
