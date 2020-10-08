from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from server.tool.response_handler import simple_response, fail_response, success_response, err_response
from server.user.model import User


@require_http_methods(["POST"])
@simple_response
def user_register(request):
    content = request.POST
    username, nickname, password = content.get("username"), content.get("nickname"), content.get("password")
    if User.objects.filter(username=username):
        return fail_response("not has such username")
    user = User()
    user.Config(username, nickname, password)
    user.save()
    return success_response("success register")


@require_http_methods(["GET"])
@simple_response
def user_login(request):
    content = request.GET
    username, password = content.get("username"), content.get("password")

    if not username or not password:
        return fail_response("username or password is null")
    if not User.objects.filter(username=username):
        return fail_response("username or password is error")
    user = User.objects.get(username=username)
    if not user.password == password:
        return fail_response("username or password is error")

    return success_response("success login")


@require_http_methods(["PUT"])
@simple_response
def user_modify(request):
    content = request.POST
    username = content.get("username")
    if not username:
        return fail_response("username is null")
    if not User.objects.filter(username=username):
        return fail_response("not has such user")
    user = User.objects.get(username=username)
    for key in content.keys():
        if hasattr(user, key):
            value = content.get(key)
            setattr(user, key, value)
    user.save()
    return success_response("success modify")


@require_http_methods(["GET"])
def user_get(request):
    content = request.GET
    response = {}
    try:
        username = content.get("username")
        if not User.objects.filter(username=username):
            response = fail_response("has such username")
            return
        response = user_message(response, username)
    except Exception as e:
        response = err_response(e)
    finally:
        return JsonResponse(response)


def user_message(response, username):
    user = User.objects.get(username=username)
    response["username"] = username
    response["nickname"] = user.nickname
    response["password"] = user.password
    return response
