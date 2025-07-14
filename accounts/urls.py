from django.urls import path,include

from . import views

app_name = 'accounts'#这个模块的名字
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]#应用级url模式配置