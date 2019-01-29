from django import forms
from django.utils import timezone

from .models import *

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'tag', 'text')

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text')