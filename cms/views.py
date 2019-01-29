from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import *

def index(request):
	post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'cms/index.html', {'post': post})

def cms_index(request):
	last_posts = Post.objects.filter(published_date__lte=timezone.now())
	posted_count = len(last_posts)
	comments_approved = Comment.objects.filter(approved_comment=True)
	comments_count = len(comments_approved)
	comments_to_approve = Comment.objects.filter(approved_comment=False).order_by('-created_date')[:3]
	last_posts_3 = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
	return render(request, 'cms/cms_index.html', {'posted_count': posted_count, 'last_posts_3': last_posts_3, 'comments_count': comments_count, 'comments_to_approve': comments_to_approve})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'cms/post_detail.html', {'post': post})

def post_detail_cms(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'cms/post_detail_cms.html', {'post': post})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail_cms', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'cms/cms_addpost.html', {'form': form})

def add_post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail_cms', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'cms/cms_addpost.html', {'form': form})

def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail_cms', pk=post.pk)

def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')

def post_list(request):
	post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	drafts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'cms/post_list.html', {'post_list': post_list, 'drafts': drafts})

def add_comment(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'cms/add_comment.html', {'form': form})

def comment_approve(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.approve()
	return redirect('index_cms')

def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.delete()
	return redirect('post_detail_cms', pk=comment.post.pk)