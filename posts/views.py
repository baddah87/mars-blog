from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post


# Create your views here.
def post_create(request):
	return render (request, 'create.html', {})
	

def post_list(request):
	post_list= Post.objects.all()
	context = {
	"list": post_list
	}
	return render(request, 'post_list.html', context)


def post_detail(request, post_id):
	obj = get_object_or_404(Post, id=post_id) 
	context= {
	"instance": obj,
	}

	return render(request, 'post_detail.html', context)

