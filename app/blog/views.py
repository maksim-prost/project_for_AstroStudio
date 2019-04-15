from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Post

def hello(request):
	bound_form = PostForm(request.POST)
	if bound_form.is_valid():
		bound_form.save()
	return render(request,'blog/post.html',context={'form':PostForm(),'posts':Post.objects.all()[::-1]})
# Create your views here.
