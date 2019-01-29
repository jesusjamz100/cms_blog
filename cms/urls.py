from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('cms/', views.cms_index, name='index_cms'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('cms/addpost', views.add_post, name='add_post'),
	path('cms/posts', views.post_list, name='post_list'),
	path('cms/posts/<int:pk>/', views.post_detail_cms, name='post_detail_cms'),
	path('cms/posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('cms/posts/<int:pk>/publish/', views.post_publish, name='post_publish'),
	path('cms/posts/<int:pk>/remove/', views.post_remove, name='post_remove'),
	path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
	path('cms/posts/<int:pk>/comment/approve', views.comment_approve, name='comment_approve'),
	path('cms/posts/<int:pk>/comment/remove', views.comment_remove, name='comment_remove')
]