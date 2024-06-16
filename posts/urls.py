from django.contrib import admin
from django.urls import path, include  # 引用include函式
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')) #新增應用程式的網址
]