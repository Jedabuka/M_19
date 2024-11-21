from django.shortcuts import render
from django.core.paginator import Paginator
from task5.models import Post

def post_page(request):
    posts = Post.objects.all().order_by('-date_time')
    items_per_page = request.GET.get('items_per_page', 3)
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts,
               'page_obj': page_obj,
               'items_per_page': items_per_page}

    return render(request, 'post_page.html', context)
