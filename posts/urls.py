from django.urls import path
from . import views
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, TempView

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post'),
    path('post/create/', PostCreate.as_view(), name='post-create'),
    path('post/update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
    path('', TempView.as_view(), name='home'),
    ]