from django import forms
from .models import Post

class PostForm(forms.Form):
	text = forms.CharField()
	def save(self):
		return Post.objects.create(
			text=self.cleaned_data['text'])
