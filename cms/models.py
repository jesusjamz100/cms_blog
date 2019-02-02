from django.db import models
from django.utils import timezone

class Usuario(models.Model):
	username = models.CharField("Username", max_length=25, unique=True, blank=False)
	name = models.CharField("Nombre", max_length=35, blank=False)
	last_name = models.CharField("Apellido", max_length=35, blank=False)
	email = models.EmailField("Email", max_length=35, blank=False)

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default="admin")
	title = models.CharField("Título", max_length=35)
	tag = models.CharField("Etiqueta", max_length=15)
	text = models.TextField("Contenido")
	created_date = models.DateTimeField("Fecha de creación", default=timezone.now)
	published_date = models.DateTimeField("Fecha de publicación", blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

	def __str__(self):
		return "{0}, {1}".format(self.title, self.tag)

class Comment(models.Model):
	post = models.ForeignKey('cms.Post', related_name='comments', on_delete=models.CASCADE)
	author = models.CharField("Autor", max_length=30)
	text = models.CharField("Contenido", max_length=500)
	created_date = models.DateTimeField("Fecha de creación", default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return "{0}, {1}".format(self.author, self.post)