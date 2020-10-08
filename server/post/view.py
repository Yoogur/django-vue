import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from server.post.model import Post
from server.tool.response_handler import simple_response, success_response, fail_response, err_response


@require_http_methods(["POST"])
@simple_response
def post_publish(request):
    post = Post()
    content = request.POST
    title, content = content.get('title'), content.get("content")
    if not title or not len(title.replace(" ", "")):
        return fail_response("has null title")
    post.config(title, content)
    post.save()
    return success_response("success publish")


@require_http_methods(["DELETE"])
@simple_response
def post_del(request):
    content = request.GET
    postId = content.get('postId')
    if not Post.objects.filter(id=postId):
        return fail_response("this post not exits")
    post = Post.objects.get(id=postId)
    post.delete()
    return success_response("success delete")


# 未实现
@require_http_methods(["GET"])
def show_posts(request):
    response = {}
    try:
        posts = Post.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", posts))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def get_by_title(request):
    content = request.GET
    response = {}
    try:
        title = content.get("title")
        if not Post.objects.filter(post_title=title):
            response = fail_response("not exits")
            return
        post = Post.objects.get(post_title=title)
        response["title"] = title
        response["content"] = post.post_content
    except Exception as e:
        response = err_response(e)
    finally:
        return JsonResponse(response)
