from django.db import models

#为学习笔记项目创建的模型
class Topic(models.Model):#继承模型类model.Model
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

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
