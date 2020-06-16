from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
	body = models.TextField()
	date = models.DateField(auto_now_add=True)
	
	def snippet(self):
		return self.body[:50] + '...'