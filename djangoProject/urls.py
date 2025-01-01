from django.contrib import admin
from django.urls import path
from project import views  # Import کردن نما
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('create/', views.create_post, name='create_post'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # اینجا ID پست رو می‌گیریم
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
]
