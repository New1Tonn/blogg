from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
from .form import CommentsForm
from .models import Comments
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import redirect

class PostView(View):
    '''вывод записей'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/dlog.html', {'post_list': posts})


class PostDetail(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})

class AddComments(View):
    '''добавление комментариев'''
    def post(self, request, pk,):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

class DeleteComment(View):
    '''удаление комментария'''

    def get(self, request, comment_id):
        comment = get_object_or_404(Comments, id=comment_id)

        # Проверяем наличие комментария
        if comment:
            # Дополнительные проверки, если необходимо
            post_id = comment.post_id
            comment.delete()
            return redirect(f'/{post_id}')
        else:
            # Обработка случая, если комментарий не найден
            return HttpResponseNotFound("Comment not found.")
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')

