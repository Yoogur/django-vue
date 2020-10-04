from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from server.user.model import User


@require_http_methods(["POST"])
def user_register(request):
    response = {}
    try:
        user = User()
        post = request.POST
        user.Config(post.get("username"), post.get("nickname"), post.get("password"))
        user.save()
        response['result'] = True
        response['msg'] = "success"
    except Exception as e:
        response['result'] = False
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def user_login(request):
    response = {}
    try:
        post = request.GET
        username, password = post.get("username"), post.get("password")
        user = User.objects.get(username=username)
        if not user.password == password:
            response['result'] = False
            response['msg'] = "username or password is error"
        else:
            response['result'] = True
            response['msg'] = 'success login'
    except Exception as e:
        response['result'] = False
        response['msg'] = str(e)
    return JsonResponse(response)
