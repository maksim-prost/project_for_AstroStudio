from django.db import models

# Create your models here.
class Post(models.Model):
	#id_pub = models.IntegerField(unique=True)
	text = models.TextField()
	date_pub = models.DateTimeField(auto_now_add=True)

