from django.shortcuts import render
from .models import Post
from .models import garanty
from django.utils import timezone
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(intime__lte=timezone.now()).order_by('ddate')
    return render(request, 'blog/start_timedgt.html', {'posts': posts})
    
def post_list1(request):
    gran = garanty.objects.filter(start__lte=timezone.now().order_by('stop'))
    return render(request, 'blog/start_timedgt.html', {'grans': gran})