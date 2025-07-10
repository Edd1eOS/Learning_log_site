from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic)#简单解释：注册Topic模型
admin.site.register(Entry)#简单解释：注册Entry模型
