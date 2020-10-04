import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from server.post.model import Post


@require_http_methods(["GET"])
def add_post(request):
    response = {}
    try:
        post = Post(post_title=request.GET.get('post_title'))
        post.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_posts(request):
    response = {}
    try:
        posts = Post.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", posts))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)